import { CommonModule } from '@angular/common';
import { ChangeDetectionStrategy, Component, ViewChild, OnDestroy, OnInit } from '@angular/core';
import { FullCalendarModule, FullCalendarComponent } from '@fullcalendar/angular';
import { CalendarOptions, EventInput } from '@fullcalendar/core';
import { C } from '@fullcalendar/core/internal-common';
import timeGridPlugin from '@fullcalendar/timegrid';
import { TranslateModule } from '@ngx-translate/core';
import { addHours, format, setHours, startOfDay } from 'date-fns';
import { BehaviorSubject, map, switchMap, forkJoin, timer, takeUntil, Subject } from 'rxjs';
import { PrimeDropdownFixDirective } from 'src/app/components/prime-dropdown-fix/prime-dropdown-fix.directive';
import { CustomPrimengModule } from 'src/app/modules/custom-primeng.module';
import { bookingColorsEnum } from 'src/app/services/api-models/booking';
import { ApiService } from 'src/app/services/api.service';
import { BranchEnum, branches } from 'src/app/services/api-models/_branch';
import { CustomerResponse } from 'src/app/services/api-models/customer';
import { UserStorageService } from 'src/app/services/user-storage.service';

@Component({
    selector: 'app-today-calendar',
    standalone: true,
    imports: [CommonModule, TranslateModule, CustomPrimengModule, FullCalendarModule, PrimeDropdownFixDirective],
    templateUrl: './today-calendar.component.html',
    changeDetection: ChangeDetectionStrategy.OnPush,
})
export class TodayCalendarComponent implements OnInit, OnDestroy {
    @ViewChild(FullCalendarComponent)
    calendar: FullCalendarComponent;

    currentDateSub$ = new BehaviorSubject(new Date());
    currentDate$ = this.currentDateSub$.asObservable().pipe(
        map((date) => ({
            date,
            isToday: date.getTime() === startOfDay(new Date()).getTime(),
        }))
    );

    branchOptions = ["All", ...branches];
    userBranch: BranchEnum | undefined;

    options: CalendarOptions;

    private selectedBranch: string | undefined;
    private unsubscribe$: Subject<void> = new Subject<void>();

    constructor(public api: ApiService, public store: UserStorageService) {
        this.options = {
            initialView: 'timeGridDay',
            plugins: [timeGridPlugin],
            slotMinTime: '07:00',
            allDaySlot: false,
            nowIndicator: true,
            // scrollTime: format(new Date(), 'HH:mm:ss'),
            height: 'auto',
            dayHeaders: false,
            headerToolbar: false,
            businessHours: {
                daysOfWeek: [0, 1, 2, 3, 4, 5, 6],
                startTime: '10:00',
                endTime: '18:30',
            },
            events: this.fetchCalendarEvents,
            eventClick: (evt) => {
                console.log(evt);
            },
        };
    }

    ngOnInit(): void {
        this.userBranch = this.store.getData().partner.branch;
        this.selectedBranch = this.userBranch === BranchEnum.PUCHONG ? "All" : this.store.getData().partner.branch;
    }

    ngOnDestroy(): void {
        this.unsubscribe$.next();
        this.unsubscribe$.complete();
    }

    updateDate(delta: number) {
        if (delta === 1) {
            this.calendar.getApi().next();
        } else if (delta === -1) {
            this.calendar.getApi().prev();
        } else {
            this.calendar.getApi().today();
        }
    }

    fetchCalendarEvents = (fetchInfo: any, successCallback: any, failureCallback: any) => {
        const startDate = new Date(fetchInfo.start);
        this.currentDateSub$.next(startDate);

        if (this.selectedBranch === 'All') {
            this.getAllBookings(fetchInfo, successCallback, failureCallback);
        } else {
            this.getBookingsByBranch(fetchInfo, successCallback, failureCallback);
        }
    }

    getAllBookings(fetchInfo: any, successCallback: any, failureCallback: any) {
        this.api
            .getBookings({
                booking_date_after: fetchInfo.start.toISOString(),
                booking_date_before: fetchInfo.end.toISOString(),
            })
            .pipe(
                switchMap((data) => {
                    const bookings = data.results;
                    const eventInput$ = bookings.map((booking) =>
                        this.api.getCustomer(booking.vehicle).pipe(
                            map((customer) => {
                                const title = `(${customer.car_plate}) ${customer.car_brand} - ${booking.remark}`;
                                return {
                                    id: booking.uuid,
                                    start: new Date(booking.booking_date),
                                    end: addHours(new Date(booking.booking_date), booking.booking_duration),
                                    title: title,
                                    editable: false,
                                    color: bookingColorsEnum[booking.booking_type],
                                };
                            })
                        )
                    );
                    return forkJoin(eventInput$);
                })
            )
            .subscribe({
                next: (data) => {
                    successCallback(data);
                },
                error: (err) => {
                    console.error(err);
                    failureCallback(err);
                },
            });
    }

    getBookingsByBranch(fetchInfo: any, successCallback: any, failureCallback: any) {
        this.api
            .getBookingsByBranch({
                branch: this.selectedBranch,
                booking_date_after: fetchInfo.start.toISOString(),
                booking_date_before: fetchInfo.end.toISOString(),
            }).pipe(
                takeUntil(this.unsubscribe$)
            ).subscribe({
                next: (data) => {
                    const bookings = data.results;
                    const eventSources = bookings?.map((customer: CustomerResponse) => {
                        const title = `(${customer.car_plate}) ${customer.car_brand} - ${customer.bookings[0].remark}`;
                        return {
                          id: customer.uuid,
                          start: new Date(customer.bookings[0].booking_date),
                          end: addHours(new Date(customer.bookings[0].booking_date), customer.bookings[0].booking_duration),
                          title: title,
                          editable: false,
                          color: bookingColorsEnum[customer.bookings[0].booking_type as keyof typeof bookingColorsEnum],
                        };
                      });
                    successCallback(eventSources);
                },
                error: (err) => {
                    console.error(err);
                    failureCallback(err);
                },
            });
    }

    onDropdownChange(event: HTMLSelectElement) {
        this.selectedBranch = event.value;
        this.calendar.getApi().removeAllEvents();
        this.calendar.getApi().refetchEvents();
    }
}

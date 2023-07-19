import { CommonModule } from '@angular/common';
import { ChangeDetectionStrategy, Component, ViewChild, AfterViewInit } from '@angular/core';
import { FullCalendarModule, FullCalendarComponent } from '@fullcalendar/angular';
import { CalendarOptions, EventInput } from '@fullcalendar/core';
import { C } from '@fullcalendar/core/internal-common';
import timeGridPlugin from '@fullcalendar/timegrid';
import { TranslateModule } from '@ngx-translate/core';
import { addHours, format, setHours, startOfDay } from 'date-fns';
import { BehaviorSubject, map, switchMap, forkJoin, timer } from 'rxjs';
import { CustomPrimengModule } from 'src/app/modules/custom-primeng.module';
import { bookingColorsEnum } from 'src/app/services/api-models/booking';
import { ApiService } from 'src/app/services/api.service';

@Component({
    selector: 'app-today-calendar',
    standalone: true,
    imports: [CommonModule, TranslateModule, CustomPrimengModule, FullCalendarModule],
    templateUrl: './today-calendar.component.html',
    changeDetection: ChangeDetectionStrategy.OnPush,
})
export class TodayCalendarComponent implements AfterViewInit {
    @ViewChild(FullCalendarComponent)
    calendar: FullCalendarComponent;

    currentDateSub$ = new BehaviorSubject(new Date());
    currentDate$ = this.currentDateSub$.asObservable().pipe(
        map((date) => ({
            date,
            isToday: date.getTime() === startOfDay(new Date()).getTime(),
        }))
    );

    options: CalendarOptions = {
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
        events: (fetchInfo, successCallback, failureCallback) => {
            const startDate = new Date(fetchInfo.start);
            this.currentDateSub$.next(startDate);

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
        },
        eventClick: (evt) => {
            console.log(evt);
        },
    };

    constructor(public api: ApiService) {}

    ngAfterViewInit(): void {}

    updateDate(delta: number) {
        if (delta === 1) {
            this.calendar.getApi().next();
        } else if (delta === -1) {
            this.calendar.getApi().prev();
        } else {
            this.calendar.getApi().today();
        }
    }
}

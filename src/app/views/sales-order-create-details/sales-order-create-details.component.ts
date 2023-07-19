import { CommonModule } from '@angular/common';
import { ChangeDetectionStrategy, Component, OnInit } from '@angular/core';
import { NonNullableFormBuilder, ReactiveFormsModule, Validators } from '@angular/forms';
import { Router, RouterModule } from '@angular/router';
import { TranslateModule, TranslateService } from '@ngx-translate/core';
import { addHours } from 'date-fns';
import { MessageService } from 'primeng/api';
import { BehaviorSubject, Observable, debounceTime, distinctUntilChanged, map, startWith, switchMap } from 'rxjs';
import { BackClickDirective } from 'src/app/components/back-click/back-click.directive';
import { BooleanFieldComponent } from 'src/app/components/form/boolean-field/boolean-field.component';
import { CustomPrimengModule } from 'src/app/modules/custom-primeng.module';
import { BookingResponse, IBookingTypeValues, bookingTypeEnum } from 'src/app/services/api-models/booking';
import { CustomerResponse } from 'src/app/services/api-models/customer';
import { SalesOrderRequest, assignedTeamEnum, customerRequirementEnum } from 'src/app/services/api-models/sales-order';
import { ApiService } from 'src/app/services/api.service';
import { enumToOptions, getEnumKeyFromValue } from 'src/app/utility/enum-to-options';

const customerRequirementOptions = enumToOptions(customerRequirementEnum, 'trait_option');
const assignedTeamOptions = enumToOptions(assignedTeamEnum, 'assigned_team_option');

export interface BookingResponseWithEndDate extends BookingResponse {
    booking_date_end: Date;
}

@Component({
    selector: 'app-sales-order-create-details',
    standalone: true,
    imports: [
        CommonModule,
        CustomPrimengModule,
        BackClickDirective,
        ReactiveFormsModule,
        TranslateModule,
        RouterModule,
        BooleanFieldComponent,
    ],
    templateUrl: './sales-order-create-details.component.html',
    changeDetection: ChangeDetectionStrategy.OnPush,
})
export class SalesOrderCreateDetailsComponent implements OnInit {
    customerRequirementOptions = customerRequirementOptions;
    assignedTeamOptions = assignedTeamOptions;

    carPlateFilterChange$ = new BehaviorSubject('');
    carPlateOptions$: Observable<CustomerResponse[]>;
    bookingOptions$: Observable<BookingResponseWithEndDate[]>;

    form = this.fb.group({
        car_plate: this.fb.control('', [Validators.required]),
        booking: this.fb.group({
            uuid: this.fb.control('', [Validators.required]),
        }),

        installment_plan: this.fb.control(false),
        cust_requirement: this.fb.control(customerRequirementOptions[0].value),
        assigned_team: this.fb.control(assignedTeamOptions[0].value),
    });

    constructor(
        public fb: NonNullableFormBuilder,
        public translate: TranslateService,
        public api: ApiService,
        public router: Router,
        public msg: MessageService
    ) {}

    ngOnInit(): void {
        this.carPlateOptions$ = this.carPlateFilterChange$.pipe(
            map((carPlate) => carPlate || ''),
            debounceTime(200),
            distinctUntilChanged(),
            switchMap((car_plate) => this.api.getCustomers(1, { car_plate, is_active: 'true' })),
            map((res) => res.results),
            startWith([])
        );

        this.bookingOptions$ = this.form.controls.car_plate.valueChanges.pipe(
            switchMap((uuid) => this.api.getCustomer(uuid)),
            map((customer) =>
                customer.bookings
                    .filter(({ is_active }) => is_active)
                    .map((booking) => ({
                        ...booking,
                        booking_date_end: addHours(new Date(booking.booking_date), booking.booking_duration),
                    }))
            )
        );
    }

    getBookingTypeText(bookingType: IBookingTypeValues) {
        return 'booking_type_option.' + getEnumKeyFromValue(bookingTypeEnum, bookingType);
    }

    saveSalesOrder() {
        if (this.form.invalid) {
            this.translate.get(['error_on_form', 'error_on_form_message']).subscribe((data) => {
                this.msg.add({
                    severity: 'error',
                    summary: data.error_on_form,
                    detail: data.error_on_form_message,
                    life: 5000,
                });
            });

            return;
        }

        const { car_plate, ...formVal } = this.form.getRawValue();
        const salesOrderData: SalesOrderRequest = {
            ...formVal,
            orders: [],
        };

        this.api.createSalesOrder(salesOrderData).subscribe((data) => {
            this.router.navigate(['/dashboard/sales-order/create/orders', data.uuid], { replaceUrl: true });
        });
    }
}

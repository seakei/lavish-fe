import { CommonModule } from '@angular/common';
import { HttpErrorResponse } from '@angular/common/http';
import { ChangeDetectionStrategy, Component, OnInit } from '@angular/core';
import { FormGroup, FormsModule, NonNullableFormBuilder, ReactiveFormsModule, Validators } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { TranslateModule, TranslateService } from '@ngx-translate/core';
import { roundToNearestMinutes } from 'date-fns';
import { MessageService } from 'primeng/api';
import { defer } from 'rxjs';
import { BackClickDirective } from 'src/app/components/back-click/back-click.directive';
import { PrimeDropdownFixDirective } from 'src/app/components/prime-dropdown-fix/prime-dropdown-fix.directive';
import { brands } from 'src/app/data/car-models';
import { sources } from 'src/app/data/customer-sources';
import { languages } from 'src/app/data/languages';
import { packages } from 'src/app/data/packages';
import { CustomPrimengModule } from 'src/app/modules/custom-primeng.module';
import { BranchEnum, branches } from 'src/app/services/api-models/_branch';
import { IBookingTypeValues, bookingTypeEnum } from 'src/app/services/api-models/booking';
import { CustomerResponse } from 'src/app/services/api-models/customer';
import { IProfileStatusValues, IRoleValues, profileStatusEnum, roleEnum } from 'src/app/services/api-models/partner';
import { ApiService } from 'src/app/services/api.service';
import { enumToOptions } from 'src/app/utility/enum-to-options';

const bookingOptions = enumToOptions(bookingTypeEnum, 'booking_type_option');

@Component({
    selector: 'app-customers-create',
    standalone: true,
    imports: [
        CommonModule,
        CustomPrimengModule,
        BackClickDirective,
        ReactiveFormsModule,
        FormsModule,
        TranslateModule,
        PrimeDropdownFixDirective,
    ],
    templateUrl: './customers-create.component.html',
    changeDetection: ChangeDetectionStrategy.OnPush,
})
export class CustomersCreateComponent implements OnInit {
    branchOptions = branches;
    packageOptions = packages;
    languageOptions = languages;
    sourceOptions = sources;
    brandOptions = brands;
    bookingOptions = bookingOptions;

    startBookingDate = roundToNearestMinutes(new Date(), { nearestTo: 10, roundingMethod: 'ceil' });

    form = this.fb.group({
        uuid: this.fb.control(''),
        car_plate: this.fb.control('', [Validators.required, Validators.pattern(/^[A-Za-z0-9 ]+$/)]),
        car_brand: this.fb.control(brands[0]),
        branch: this.fb.control(BranchEnum.PUCHONG),
        package: this.fb.control(packages[0]),
        remarks: this.fb.control(''),
        bookings: this.fb.array([this.getBookingFormGroup(this.startBookingDate, null)]),
        is_active: this.fb.control(true),

        partner: this.fb.group({
            uuid: this.fb.control(''),
            phone_number: this.fb.control('', [Validators.required]),
            name: this.fb.control('', [Validators.required]),
            email: this.fb.control('', [Validators.required, Validators.email]),
            language: this.fb.control(languages[0].code),
            address: this.fb.control(''),
            customer_from: this.fb.control(sources[0]),
            role: this.fb.control<IRoleValues>(roleEnum.Customer),
            profile_status: this.fb.control<IProfileStatusValues>(profileStatusEnum.NEW),
        }),
    });

    constructor(
        public fb: NonNullableFormBuilder,
        public api: ApiService,
        public msg: MessageService,
        public translate: TranslateService,
        public router: Router,
        public activatedRoute: ActivatedRoute
    ) {}

    ngOnInit(): void {
        const existingCustomer: CustomerResponse = this.activatedRoute.snapshot.data['existingCustomer'];
        if (existingCustomer) {
            const { bookings, ...restExistingCustomer } = existingCustomer;
            this.form.patchValue(restExistingCustomer);

            this.form.controls.bookings.clear();
            bookings
                .filter(({ is_active }) => is_active)
                .forEach(({ booking_date, follow_up_date, ...restBooking }) => {
                    const group = this.getBookingFormGroup(
                        new Date(booking_date),
                        follow_up_date ? new Date(follow_up_date) : null
                    );
                    group.patchValue(restBooking);
                    this.form.controls.bookings.push(group);
                });

            this.form.controls.car_plate.disable();
        }
    }

    getBookingFormGroup(initBookingDate: Date, initFollowUpDate: Date | null) {
        const group = this.fb.group({
            uuid: this.fb.control(''),
            booking_date: this.fb.control<Date>(initBookingDate, [Validators.required]),
            follow_up_date: this.fb.control<Date | null>(initFollowUpDate),
            is_active: this.fb.control(true),
            booking_duration: this.fb.control(0),
            booking_type: this.fb.control<IBookingTypeValues>(bookingOptions[0].value),
            remark: this.fb.control(''),
        });

        return group;
    }

    getActiveBookings() {
        return this.form.controls.bookings.controls.filter((group) => group.controls.is_active.value);
    }

    addToArray() {
        this.form.controls.bookings.push(this.getBookingFormGroup(this.startBookingDate, null));
    }

    calculateBookingEndTime(group: FormGroup) {
        const startTime = group.get('booking_date')!.value as Date;
        const duration = (group.get('booking_duration')!.value as number) || 0;

        if (startTime && duration > 0) {
            const cloneDate = new Date(startTime);
            cloneDate.setMinutes(cloneDate.getMinutes() + duration * 60);
            return cloneDate.toLocaleString(undefined, { hour12: false, dateStyle: 'short', timeStyle: 'short' });
        } else {
            return '';
        }
    }

    save() {
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

        const data = this.form.getRawValue();
        data.car_plate = data.car_plate.toUpperCase().replace(/[^A-Z0-9]/g, '');

        defer(() => {
            if (data.uuid === '') {
                return this.api.createCustomer(data);
            }

            return this.api.patchCustomer(data);
        }).subscribe({
            next: () => {
                this.router.navigate(['/dashboard/customers']);
            },
            error: (err: HttpErrorResponse) => {
                console.error(err);

                const summary = 'error_on_form';
                let detail = 'error_on_form_server';

                const errors: any = err.error;
                if (errors?.car_plate) {
                    detail = 'error_car_plate_already_exists';
                    this.form.controls.car_plate.setErrors({ exist: true });
                }

                this.msg.add({
                    severity: 'error',
                    summary: this.translate.instant(summary),
                    detail: this.translate.instant(detail),
                    life: 5000,
                });
            },
        });
    }
}

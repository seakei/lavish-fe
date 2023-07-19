import { CommonModule } from '@angular/common';
import { ChangeDetectionStrategy, Component, Input, OnInit } from '@angular/core';
import { FormGroup, FormsModule, ReactiveFormsModule } from '@angular/forms';
import { TranslateModule, TranslateService } from '@ngx-translate/core';
import { CustomPrimengModule } from 'src/app/modules/custom-primeng.module';
import { OrderTypeEnum } from 'src/app/services/api-models/order';
import { ItemNameEnum, JobTypeEnum } from 'src/app/services/api-models/order-item';
import { enumToOptions, getEnumKeyFromValue } from 'src/app/utility/enum-to-options';
import { OrderFormGroup } from 'src/app/views/sales-order-create/get-order-items';
import { BooleanFieldComponent } from '../form/boolean-field/boolean-field.component';

const jobTypeOptions = enumToOptions(JobTypeEnum, 'job_type_option');
const itemNameOptions = enumToOptions(ItemNameEnum, '');

@Component({
    selector: 'app-order-form-group',
    standalone: true,
    imports: [
        CommonModule,
        CustomPrimengModule,
        TranslateModule,
        ReactiveFormsModule,
        FormsModule,
        BooleanFieldComponent,
    ],
    templateUrl: './order-form-group.component.html',
    changeDetection: ChangeDetectionStrategy.OnPush,
})
export class OrderFormGroupComponent implements OnInit {
    @Input() orderFormGroup: FormGroup<OrderFormGroup>;
    @Input() orderType: OrderTypeEnum;

    jobTypeOptions = jobTypeOptions;
    itemNameOptions = itemNameOptions;

    constructor(public translate: TranslateService) {}

    ngOnInit(): void {}

    getJobTypeLabel(searchVal: JobTypeEnum[]) {
        return searchVal
            .map((val) => getEnumKeyFromValue(JobTypeEnum, val))
            .map((val) => `job_type_option.${val}`)
            .map((val) => this.translate.instant(val))
            .join(', ');
    }
}

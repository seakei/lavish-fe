import { CommonModule } from '@angular/common';
import { ChangeDetectionStrategy, Component, OnDestroy, OnInit } from '@angular/core';
import { FormsModule, NonNullableFormBuilder, ReactiveFormsModule, Validators } from '@angular/forms';
import { TranslateModule } from '@ngx-translate/core';
import { DynamicDialogRef } from 'primeng/dynamicdialog';
import { Subscription } from 'rxjs';
import { CustomPrimengModule } from 'src/app/modules/custom-primeng.module';
import { OrderModeEnum, OrderRequest, OrderTypeEnum, ProductPackageEnum } from 'src/app/services/api-models/order';
import { enumToOptions } from 'src/app/utility/enum-to-options';
import { productMap } from 'src/app/utility/product-map';
import { OrderFormGroup } from 'src/app/views/sales-order-create/get-order-items';

const orderTypeOptions = enumToOptions(OrderTypeEnum, 'order_type_option');
const orderModeOptions = enumToOptions(OrderModeEnum, 'order_mode_option');
const productPackageOptions = enumToOptions(ProductPackageEnum, '');

@Component({
    selector: 'app-add-into-order-dialog',
    standalone: true,
    imports: [CommonModule, CustomPrimengModule, TranslateModule, ReactiveFormsModule, FormsModule],
    templateUrl: './add-into-order-dialog.component.html',
    changeDetection: ChangeDetectionStrategy.OnPush,
})
export class AddIntoOrderDialogComponent implements OnInit, OnDestroy {
    orderTypeEnum = OrderTypeEnum;
    orderModeEnum = OrderModeEnum;

    orderTypeOptions = orderTypeOptions;
    orderModeOptions = orderModeOptions;
    productPackageOptions = productPackageOptions;

    orderModeValChangeSub: Subscription;

    form = this.fb.group<Omit<OrderFormGroup, 'orderitems' | 'is_active'>>({
        uuid: this.fb.control(''),
        order_type: this.fb.control(OrderTypeEnum.TINT),
        order_mode: this.fb.control(orderModeOptions[0].value),
        product_package: this.fb.control(undefined),
    });

    constructor(public fb: NonNullableFormBuilder, public ref: DynamicDialogRef) {}

    ngOnInit(): void {
        this.orderModeValChangeSub = this.form.controls.order_mode.valueChanges.subscribe((orderModeVal) => {
            if (orderModeVal === OrderModeEnum.PACKAGE) {
                this.form.controls.product_package.addValidators(Validators.required);
            } else {
                this.form.controls.product_package.removeValidators(Validators.required);
                this.form.controls.product_package.reset(undefined);
            }
            this.form.controls.product_package.updateValueAndValidity();
        });
    }

    ngOnDestroy(): void {
        this.orderModeValChangeSub?.unsubscribe();
    }

    getPackageOptions(orderType: OrderTypeEnum) {
        let packageVals: ProductPackageEnum[] = [];

        if ([OrderTypeEnum.TINT, OrderTypeEnum.COATING, OrderTypeEnum.PPF].includes(orderType)) {
            packageVals = [...productMap.get(orderType)!.keys()];
        }

        return productPackageOptions.filter((item) => packageVals.includes(item.value));
    }

    generate() {
        if (this.form.invalid) {
            return;
        }

        const formVal = this.form.getRawValue();
        const order: OrderRequest = {
            ...formVal,
            orderitems: [],
            is_active: true,
        };

        this.ref.close(order);
    }
}

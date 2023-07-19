import { CommonModule } from '@angular/common';
import { ChangeDetectionStrategy, ChangeDetectorRef, Component, OnInit } from '@angular/core';
import { FormGroup, NonNullableFormBuilder, ReactiveFormsModule } from '@angular/forms';
import { ActivatedRoute, Router, RouterModule } from '@angular/router';
import { TranslateModule, TranslateService } from '@ngx-translate/core';
import { DialogService } from 'primeng/dynamicdialog';
import { AddIntoOrderDialogComponent } from 'src/app/components/add-into-order-dialog/add-into-order-dialog.component';
import { CustomPrimengModule } from 'src/app/modules/custom-primeng.module';
import { OrderModeEnum, OrderRequest, OrderTypeEnum, ProductPackageEnum } from 'src/app/services/api-models/order';
import { ItemNameEnum, JobTypeEnum, OrderItemRequest, VehiclePartEnum } from 'src/app/services/api-models/order-item';
import { SalesOrderResponse } from 'src/app/services/api-models/sales-order';
import { ApiService } from 'src/app/services/api.service';
import { enumToOptions, getEnumKeyFromValue } from 'src/app/utility/enum-to-options';
import {
    OrderFormGroup,
    getOrderFormGroup,
    getOrderItemFormGroup,
    getOrderItemFormGroupForTint,
} from '../sales-order-create/get-order-items';

const orderTypeOptions = enumToOptions(OrderTypeEnum, 'order_type_option');
const orderModeOptions = enumToOptions(OrderModeEnum, 'order_mode_option');
const productPackageOptions = enumToOptions(ProductPackageEnum, '');

const vehiclePartOptions = enumToOptions(VehiclePartEnum, 'vehicle_part_option');
const jobTypeOptions = enumToOptions(JobTypeEnum, 'job_type_option');
const itemNameOptions = enumToOptions(ItemNameEnum, '');

@Component({
    selector: 'app-sales-order-create-order',
    standalone: true,
    imports: [CommonModule, CustomPrimengModule, ReactiveFormsModule, TranslateModule, RouterModule],
    templateUrl: './sales-order-create-order.component.html',
    changeDetection: ChangeDetectionStrategy.OnPush,
    providers: [DialogService],
})
export class SalesOrderCreateOrderComponent implements OnInit {
    form = this.fb.group({
        orders: this.fb.array<FormGroup<OrderFormGroup>>([]),
    });
    salesOrder: SalesOrderResponse = this.activatedRoute.snapshot.data['existingSalesOrder'];

    orderTypeOptions = orderTypeOptions;
    orderModeOptions = orderModeOptions;
    productPackageOptions = productPackageOptions;
    orderModeEnum = OrderModeEnum;

    vehiclePartOptions = vehiclePartOptions;
    jobTypeOptions = jobTypeOptions;
    itemNameOptions = itemNameOptions;

    constructor(
        public fb: NonNullableFormBuilder,
        public activatedRoute: ActivatedRoute,
        public dialog: DialogService,
        public translate: TranslateService,
        public cdr: ChangeDetectorRef,
        public api: ApiService,
        public router: Router
    ) {}

    ngOnInit(): void {
        this.salesOrder.orders
            .filter(({ is_active }) => is_active)
            .forEach((order) => {
                const orderFormGroup = getOrderFormGroup(this.fb, order);
                order.orderitems.forEach((orderItem) => {
                    const orderItemFormGroup = getOrderItemFormGroup(this.fb, orderItem);
                    orderFormGroup.controls.orderitems.push(orderItemFormGroup);
                });

                this.form.controls.orders.push(orderFormGroup);
            });
    }

    openAddIntoOrderDialog() {
        this.dialog
            .open(AddIntoOrderDialogComponent, {
                header: this.translate.instant('sales_order.add_order'),
                modal: true,
                styleClass: 'p-dialog__sm',
            })
            .onClose.pipe()
            .subscribe((order?: OrderRequest) => {
                if (!order) {
                    return;
                }

                const orderFormGroup = this.fb.group<OrderFormGroup>({
                    uuid: this.fb.control(''),
                    order_type: this.fb.control(order.order_type),
                    order_mode: this.fb.control(order.order_mode),
                    product_package: this.fb.control(order.product_package),
                    orderitems: getOrderItemFormGroupForTint(this.fb, order, undefined),
                    is_active: this.fb.control(order.is_active),
                });

                this.form.controls.orders.push(orderFormGroup);
                this.cdr.markForCheck();
            });
    }

    getActiveOrders() {
        return this.form.controls.orders.controls.filter((group) => group.controls.is_active.value);
    }

    getActiveOrderItems(orderItemFormGroup: OrderFormGroup['orderitems']) {
        return orderItemFormGroup.controls.filter((group) => group.controls.is_active.value);
    }

    getOrderHeader(activeOrderIdx: number, orderVal: OrderRequest) {
        const orderNumber = this.translate.instant('sales_order.order_count') + ` #${activeOrderIdx + 1}`;
        const orderType = 'order_type_option.' + getEnumKeyFromValue(OrderTypeEnum, orderVal.order_type);
        const orderMode = 'order_mode_option.' + getEnumKeyFromValue(OrderModeEnum, orderVal.order_mode);
        return `${orderNumber} - ${this.translate.instant(orderType)}, ${this.translate.instant(orderMode)}`;
    }

    getOrderItemsHeader(orderItemVal: OrderItemRequest) {
        const vehiclePart = 'vehicle_part_option.' + getEnumKeyFromValue(VehiclePartEnum, orderItemVal.vehicle_part);
        return this.translate.instant(vehiclePart);
    }

    addOrderItem(orderItemFormGroup: OrderFormGroup['orderitems']) {
        const orderItemForm = getOrderItemFormGroup(this.fb, {
            vehicle_part: VehiclePartEnum.FRONT_WINDSCREEN,
            job_type: [JobTypeEnum.DO_IT_NOW, JobTypeEnum.INSTALL],
            item_name: itemNameOptions[0].value,
            claim_insurance: false,
            remarks: '',
            is_active: true,
        });
        orderItemFormGroup.push(orderItemForm);
    }

    getJobTypeLabel(searchVal: JobTypeEnum[]) {
        return searchVal
            .map((val) => getEnumKeyFromValue(JobTypeEnum, val))
            .map((val) => `job_type_option.${val}`)
            .map((val) => this.translate.instant(val))
            .join(', ');
    }

    saveSalesOrder() {
        const formVal = this.form.getRawValue();
        // if (formVal.orders.some(({ orderitems }) => orderitems.length === 0)) {}

        this.api
            .patchSalesOrderWithOrders({
                uuid: this.salesOrder.uuid,
                ...formVal,
            })
            .subscribe(() => {
                this.router.navigate(['/dashboard/sales-order/create/summary', this.salesOrder.uuid]);
            });
    }
}

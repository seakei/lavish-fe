import { FormArray, FormControl, FormGroup, NonNullableFormBuilder } from '@angular/forms';
import {
    OrderRequest,
    OrderModeEnum,
    OrderTypeEnum,
    ProductPackageEnum,
    OrderResponse,
} from 'src/app/services/api-models/order';
import {
    JobTypeEnum,
    OrderItemRequest,
    ItemNameEnum,
    VehiclePartEnum,
    OrderItemResponse,
} from 'src/app/services/api-models/order-item';

export interface OrderFormGroup {
    uuid: FormControl<string>;
    order_type: FormControl<OrderTypeEnum>;
    order_mode: FormControl<OrderModeEnum>;
    product_package: FormControl<ProductPackageEnum | undefined>;
    orderitems: FormArray<FormGroup<OrderItemsFormGroup>>;
    is_active: FormControl<boolean>;
}

export interface OrderItemsFormGroup {
    uuid: FormControl<string>;
    vehicle_part: FormControl<VehiclePartEnum>;
    job_type: FormControl<JobTypeEnum[]>;
    item_name: FormControl<ItemNameEnum>;
    claim_insurance: FormControl<boolean>;
    remarks: FormControl<string>;
    is_active: FormControl<boolean>;
}

export const getOrderFormGroup = (fb: NonNullableFormBuilder, val: OrderResponse) => {
    return fb.group<OrderFormGroup>({
        uuid: fb.control(val.uuid),
        order_type: fb.control(val.order_type),
        order_mode: fb.control(val.order_mode),
        product_package: fb.control(val.product_package),
        orderitems: fb.array<FormGroup<OrderItemsFormGroup>>([]),
        is_active: fb.control(val.is_active),
    });
};

export const getOrderItemFormGroup = (fb: NonNullableFormBuilder, val: OrderItemRequest | OrderItemResponse) => {
    return fb.group<OrderItemsFormGroup>({
        uuid: fb.control(val.uuid || ''),
        vehicle_part: fb.control(val.vehicle_part),
        job_type: fb.control(val.job_type),
        item_name: fb.control(val.item_name),
        claim_insurance: fb.control(val.claim_insurance),
        remarks: fb.control(val.remarks),
        is_active: fb.control(val.is_active),
    });
};

export const getOrderItemFormGroupForTint = (
    fb: NonNullableFormBuilder,
    order: OrderRequest,
    val?: OrderItemRequest
): FormArray<FormGroup<OrderItemsFormGroup>> => {
    let parts: VehiclePartEnum[] = [];

    if (order.order_mode === OrderModeEnum.PACKAGE) {
        if (order.order_type === OrderTypeEnum.TINT) {
            parts = [
                VehiclePartEnum.FRONT_WINDSCREEN,
                VehiclePartEnum.REAR_WINDSCREEN,
                VehiclePartEnum.SIDE_WINDOW_L1,
                VehiclePartEnum.SIDE_WINDOW_L2,
                VehiclePartEnum.SIDE_WINDOW_L3,
                VehiclePartEnum.SIDE_WINDOW_R1,
                VehiclePartEnum.SIDE_WINDOW_R2,
                VehiclePartEnum.SIDE_WINDOW_R3,
                VehiclePartEnum.SUNROOF_2,
                VehiclePartEnum.SUNVISOR,
            ];
        } else if (order.order_type === OrderTypeEnum.COATING) {
            parts = [VehiclePartEnum.BODYPAINT, VehiclePartEnum.SPORT_RIM, VehiclePartEnum.WINDOWS];

            if (order.product_package === ProductPackageEnum.CRYSTAL_GLOSS_9H) {
                parts = [
                    VehiclePartEnum.BODYPAINT,
                    VehiclePartEnum.INTERIOR,
                    VehiclePartEnum.SPORT_RIM,
                    VehiclePartEnum.WINDOWS,
                ];
            } else if (order.product_package === ProductPackageEnum.MULTI_QUARTZ_9H) {
                parts = [
                    VehiclePartEnum.BODYPAINT,
                    VehiclePartEnum.HEADLIGHT_L,
                    VehiclePartEnum.HEADLIGHT_R,
                    VehiclePartEnum.INTERIOR,
                    VehiclePartEnum.SPORT_RIM,
                    VehiclePartEnum.WINDOWS,
                ];
            }
        } else if (order.order_type === OrderTypeEnum.PPF) {
            parts = [
                VehiclePartEnum.DOOR_CUP_L1,
                VehiclePartEnum.DOOR_CUP_L2,
                VehiclePartEnum.DOOR_CUP_R1,
                VehiclePartEnum.DOOR_CUP_R2,
                VehiclePartEnum.DOOR_EDGE_L1,
                VehiclePartEnum.DOOR_EDGE_L2,
                VehiclePartEnum.DOOR_EDGE_R1,
                VehiclePartEnum.DOOR_EDGE_R2,
            ];
        }
    }

    const formArr = fb.array<FormGroup<OrderItemsFormGroup>>(
        parts.map((vehicle_part) => {
            const orderItemGroup = getOrderItemFormGroup(fb, {
                uuid: val?.uuid || '',
                vehicle_part,
                job_type: val?.job_type ?? [JobTypeEnum.DO_IT_NOW, JobTypeEnum.INSTALL],
                item_name: val?.item_name || ItemNameEnum.BLACK_RAINBOWSUPER_CLEAR_3MIL,
                claim_insurance: val?.claim_insurance ?? false,
                remarks: val?.remarks || '',
                is_active: val?.is_active ?? true,
            });
            return orderItemGroup;
        })
    );

    return formArr;
};

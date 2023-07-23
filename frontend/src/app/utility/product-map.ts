import { OrderTypeEnum, ProductPackageEnum } from 'src/app/services/api-models/order';
import { VehiclePartEnum } from 'src/app/services/api-models/order-item';

// tint parts appear to be the same?
const tintParts = [
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

/*
    please follow this format :-)

    productMap.set(
        // this is the order type
        OrderTypeEnum.THE_ORDER_TYPE,

        // this is a nested map of product package to vehicle parts
        new Map([
            [
                // the first item in the array is the product package
                ProductPackageEnum.THE_PRODUCT_PACKAGE

                // the second item in the array is the vehicle parts array
                [
                    VehiclePartEnum.ONE,
                    VehiclePartEnum.TWO,
                ]
            ]

        ])
    )
*/

export const productMap = new Map<OrderTypeEnum, Map<ProductPackageEnum, VehiclePartEnum[]>>();

productMap.set(
    OrderTypeEnum.TINT,
    new Map([
        [ProductPackageEnum.TITAN, [...tintParts]],
        [ProductPackageEnum.BRONZE, [...tintParts]],
        [ProductPackageEnum.SILVER, [...tintParts]],
        [ProductPackageEnum.GOLD, [...tintParts]],
        [ProductPackageEnum.PLATINUM, [...tintParts]],
        [ProductPackageEnum.ROYAL, [...tintParts]],
        [ProductPackageEnum.ROYAL_PLUS, [...tintParts]],
        [ProductPackageEnum.ROYAL_PLUS_SAFETY, [...tintParts]],
    ])
);

productMap.set(
    OrderTypeEnum.COATING,
    new Map([
        [ProductPackageEnum.ELEMENTAL, [VehiclePartEnum.BODYPAINT]],
        [
            ProductPackageEnum.ECO_BONZ_9H,
            [VehiclePartEnum.BODYPAINT, VehiclePartEnum.SPORT_RIM, VehiclePartEnum.WINDOWS],
        ],
        [
            ProductPackageEnum.CRYSTAL_GLOSS_9H,
            [VehiclePartEnum.BODYPAINT, VehiclePartEnum.INTERIOR, VehiclePartEnum.SPORT_RIM, VehiclePartEnum.WINDOWS],
        ],
        [
            ProductPackageEnum.MULTI_QUARTZ_9H,
            [
                VehiclePartEnum.BODYPAINT,
                VehiclePartEnum.HEADLIGHT_L,
                VehiclePartEnum.HEADLIGHT_R,
                VehiclePartEnum.INTERIOR,
                VehiclePartEnum.SPORT_RIM,
                VehiclePartEnum.WINDOWS,
            ],
        ],
    ])
);

productMap.set(
    OrderTypeEnum.PPF,
    new Map([
        [
            ProductPackageEnum.AVANTGARDE,
            [
                VehiclePartEnum.DOOR_CUP_L1,
                VehiclePartEnum.DOOR_CUP_L2,
                VehiclePartEnum.DOOR_CUP_R1,
                VehiclePartEnum.DOOR_CUP_R2,
                VehiclePartEnum.DOOR_EDGE_L1,
                VehiclePartEnum.DOOR_EDGE_L2,
                VehiclePartEnum.DOOR_EDGE_R1,
                VehiclePartEnum.DOOR_EDGE_R2,
                VehiclePartEnum.FRONT_BUMPER,
            ],
        ],
        [
            ProductPackageEnum.KOSMOS_I,
            [
                VehiclePartEnum.HEADLIGHT_L,
                VehiclePartEnum.HEADLIGHT_R,
                VehiclePartEnum.FUEL_CAP,
                VehiclePartEnum.DOOR_CUP_L1,
                VehiclePartEnum.DOOR_CUP_L2,
                VehiclePartEnum.DOOR_CUP_R1,
                VehiclePartEnum.DOOR_CUP_R2,
                VehiclePartEnum.DOOR_EDGE_L1,
                VehiclePartEnum.DOOR_EDGE_L2,
                VehiclePartEnum.DOOR_EDGE_R1,
                VehiclePartEnum.DOOR_EDGE_R2,
            ],
        ],
        [
            ProductPackageEnum.KOSMOS_II,
            [
                VehiclePartEnum.HEADLIGHT_L,
                VehiclePartEnum.HEADLIGHT_R,
                VehiclePartEnum.FUEL_CAP,
                VehiclePartEnum.DOOR_CUP_L1,
                VehiclePartEnum.DOOR_CUP_L2,
                VehiclePartEnum.DOOR_CUP_R1,
                VehiclePartEnum.DOOR_CUP_R2,
                VehiclePartEnum.DOOR_EDGE_L1,
                VehiclePartEnum.DOOR_EDGE_L2,
                VehiclePartEnum.DOOR_EDGE_R1,
                VehiclePartEnum.DOOR_EDGE_R2,
                VehiclePartEnum.SIDE_MIRROR_L,
                VehiclePartEnum.SIDE_MIRROR_R,
            ],
        ],
        [
            ProductPackageEnum.KOMSOS_III,
            [
                VehiclePartEnum.HEADLIGHT_L,
                VehiclePartEnum.HEADLIGHT_R,
                VehiclePartEnum.FUEL_CAP,
                VehiclePartEnum.DOOR_CUP_L1,
                VehiclePartEnum.DOOR_CUP_L2,
                VehiclePartEnum.DOOR_CUP_R1,
                VehiclePartEnum.DOOR_CUP_R2,
                VehiclePartEnum.DOOR_EDGE_L1,
                VehiclePartEnum.DOOR_EDGE_L2,
                VehiclePartEnum.DOOR_EDGE_R1,
                VehiclePartEnum.DOOR_EDGE_R2,
                VehiclePartEnum.SIDE_MIRROR_L,
                VehiclePartEnum.SIDE_MIRROR_R,
                VehiclePartEnum.REAR_HEADLIGHT_L,
                VehiclePartEnum.REAR_HEADLIGHT_R,
            ],
        ],
        [
            ProductPackageEnum.KLEIO,
            [
                VehiclePartEnum.HEADLIGHT_L,
                VehiclePartEnum.HEADLIGHT_R,
                VehiclePartEnum.FUEL_CAP,
                VehiclePartEnum.DOOR_CUP_L1,
                VehiclePartEnum.DOOR_CUP_L2,
                VehiclePartEnum.DOOR_CUP_R1,
                VehiclePartEnum.DOOR_CUP_R2,
                VehiclePartEnum.DOOR_EDGE_L1,
                VehiclePartEnum.DOOR_EDGE_L2,
                VehiclePartEnum.DOOR_EDGE_R1,
                VehiclePartEnum.DOOR_EDGE_R2,
                VehiclePartEnum.SIDE_MIRROR_L,
                VehiclePartEnum.SIDE_MIRROR_R,
                VehiclePartEnum.FRONT_BUMPER,
            ],
        ],
        [
            ProductPackageEnum.MORPHEUS,
            [
                VehiclePartEnum.HEADLIGHT_L,
                VehiclePartEnum.HEADLIGHT_R,
                VehiclePartEnum.FUEL_CAP,
                VehiclePartEnum.DOOR_CUP_L1,
                VehiclePartEnum.DOOR_CUP_L2,
                VehiclePartEnum.DOOR_CUP_R1,
                VehiclePartEnum.DOOR_CUP_R2,
                VehiclePartEnum.DOOR_EDGE_L1,
                VehiclePartEnum.DOOR_EDGE_L2,
                VehiclePartEnum.DOOR_EDGE_R1,
                VehiclePartEnum.DOOR_EDGE_R2,
                VehiclePartEnum.SIDE_MIRROR_L,
                VehiclePartEnum.SIDE_MIRROR_R,
                VehiclePartEnum.FRONT_BUMPER,
                VehiclePartEnum.FRONT_HOOD,
            ],
        ],
        [
            ProductPackageEnum.MATTHIAS,
            [
                VehiclePartEnum.HEADLIGHT_L,
                VehiclePartEnum.HEADLIGHT_R,
                VehiclePartEnum.FUEL_CAP,
                VehiclePartEnum.DOOR_CUP_L1,
                VehiclePartEnum.DOOR_CUP_L2,
                VehiclePartEnum.DOOR_CUP_R1,
                VehiclePartEnum.DOOR_CUP_R2,
                VehiclePartEnum.DOOR_EDGE_L1,
                VehiclePartEnum.DOOR_EDGE_L2,
                VehiclePartEnum.DOOR_EDGE_R1,
                VehiclePartEnum.DOOR_EDGE_R2,
                VehiclePartEnum.SIDE_MIRROR_L,
                VehiclePartEnum.SIDE_MIRROR_R,
                VehiclePartEnum.FRONT_BUMPER,
                VehiclePartEnum.FRONT_HOOD,
                VehiclePartEnum.FRONT_FENDER_L,
                VehiclePartEnum.FRONT_FENDER_R,
                VehiclePartEnum.REAR_HEADLIGHT_L,
                VehiclePartEnum.REAR_HEADLIGHT_R,
            ],
        ],
        [
            ProductPackageEnum.MAXIMUS,
            [
                VehiclePartEnum.HEADLIGHT_L,
                VehiclePartEnum.HEADLIGHT_R,
                VehiclePartEnum.FUEL_CAP,
                VehiclePartEnum.SIDE_MIRROR_L,
                VehiclePartEnum.SIDE_MIRROR_R,
                VehiclePartEnum.FRONT_BUMPER,
                VehiclePartEnum.FRONT_HOOD,
                VehiclePartEnum.FRONT_FENDER_L,
                VehiclePartEnum.FRONT_FENDER_R,
                VehiclePartEnum.REAR_HEADLIGHT_L,
                VehiclePartEnum.REAR_HEADLIGHT_R,
                VehiclePartEnum.REAR_BUMPER,
                VehiclePartEnum.REAR_BONNET,
                VehiclePartEnum.FRONT_DOOR_L,
                VehiclePartEnum.FRONT_DOOR_R,
                VehiclePartEnum.REAR_DOOR_L,
                VehiclePartEnum.REAR_DOOR_R,
                VehiclePartEnum.ROOFTOP,
                VehiclePartEnum.SKIRTING_L,
                VehiclePartEnum.SKIRTING_R,
                VehiclePartEnum.PILLAR_AND_REAR_FENDER_L,
                VehiclePartEnum.PILLAR_AND_REAR_FENDER_R,
                VehiclePartEnum.SPOILER,
            ],
        ],
    ])
);

/*
    please follow this format :-)

    productMap.set(
        // this is the order type
        OrderTypeEnum.THE_ORDER_TYPE,

        // list of vehicle parts
        [
            VehiclePartEnum.ONE,
            VehiclePartEnum.TWO,
        ]
    )
*/
export const partMap = new Map<OrderTypeEnum, VehiclePartEnum[]>();
partMap.set(OrderTypeEnum.TINT, [
    VehiclePartEnum.FRONT_WINDSCREEN,
    VehiclePartEnum.REAR_WINDSCREEN,
    VehiclePartEnum.CANOPY_WINDOW_L,
    VehiclePartEnum.CANOPY_WINDOW_R,
    VehiclePartEnum.SIDE_WINDOW_L1,
    VehiclePartEnum.SIDE_WINDOW_L2,
    VehiclePartEnum.SIDE_WINDOW_L3,
    VehiclePartEnum.SIDE_WINDOW_R1,
    VehiclePartEnum.SIDE_WINDOW_R2,
    VehiclePartEnum.SIDE_WINDOW_R3,
    VehiclePartEnum.SUNROOF_1,
    VehiclePartEnum.SUNROOF_2,
    VehiclePartEnum.SUNVISOR,
]);

partMap.set(OrderTypeEnum.COATING, [
    VehiclePartEnum.FRONT_WINDSCREEN,
    VehiclePartEnum.REAR_WINDSCREEN,
    VehiclePartEnum.INTERIOR,
    VehiclePartEnum.HEADLIGHT_L,
    VehiclePartEnum.HEADLIGHT_R,
    VehiclePartEnum.BODYPAINT,
    VehiclePartEnum.FRONT_PART,
    VehiclePartEnum.DOOR_L1,
    VehiclePartEnum.DOOR_L2,
    VehiclePartEnum.DOOR_L3,
    VehiclePartEnum.DOOR_R1,
    VehiclePartEnum.DOOR_R2,
    VehiclePartEnum.DOOR_R3,
    VehiclePartEnum.ROOFTOP,
    VehiclePartEnum.REAR_PART,
    VehiclePartEnum.SPORT_RIM,
    VehiclePartEnum.WINDOWS,
]);
partMap.set(OrderTypeEnum.PPF, [
    VehiclePartEnum.REAR_WINDSCREEN,
    VehiclePartEnum.INTERIOR,
    VehiclePartEnum.HEADLIGHT_L,
    VehiclePartEnum.HEADLIGHT_R,
    VehiclePartEnum.DOOR_CUP_L1,
    VehiclePartEnum.DOOR_CUP_L2,
    VehiclePartEnum.DOOR_CUP_R1,
    VehiclePartEnum.DOOR_CUP_R2,
    VehiclePartEnum.DOOR_EDGE_L1,
    VehiclePartEnum.DOOR_EDGE_L2,
    VehiclePartEnum.DOOR_EDGE_R1,
    VehiclePartEnum.DOOR_EDGE_R2,
    VehiclePartEnum.FUEL_CAP,
    VehiclePartEnum.FRONT_FENDER_L,
    VehiclePartEnum.FRONT_FENDER_R,
    VehiclePartEnum.FRONT_DOOR_L,
    VehiclePartEnum.FRONT_DOOR_R,
    VehiclePartEnum.FRONT_FOGLAMP,
    VehiclePartEnum.FRONT_GRILLE,
    VehiclePartEnum.PILLAR_AND_REAR_FENDER_L,
    VehiclePartEnum.PILLAR_AND_REAR_FENDER_R,
    VehiclePartEnum.REAR_HEADLIGHT_L,
    VehiclePartEnum.REAR_HEADLIGHT_R,
    VehiclePartEnum.SKIRTING_L,
    VehiclePartEnum.SKIRTING_R,
    VehiclePartEnum.REAR_BOOT_EDGE,
    VehiclePartEnum.REAR_BUMPER,
    VehiclePartEnum.REAR_BUMPER_EDGE,
    VehiclePartEnum.REAR_BONNET,
    VehiclePartEnum.REAR_DOOR_L,
    VehiclePartEnum.REAR_DOOR_R,
    VehiclePartEnum.SIDE_MIRROR_L,
    VehiclePartEnum.SIDE_MIRROR_R,
    VehiclePartEnum.SPOILER,
    VehiclePartEnum.SIDE_STEP_L1,
    VehiclePartEnum.SIDE_STEP_L2,
    VehiclePartEnum.SIDE_STEP_R1,
    VehiclePartEnum.SIDE_STEP_R2,
]);

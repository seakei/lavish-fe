import { OrderItemRequest, OrderItemResponse } from './order-item';

export type OrderTypeEnumKeys =
    | 'ACCESSORIES'
    | 'TINT'
    | 'COATING'
    | 'PPF'
    | 'GIFT'
    | 'MVP'
    | 'ESSENTIAL'
    | 'DELUXE'
    | 'ULTIMATE'
    | 'XCA1'
    | 'XCA2'
    | 'XCA3'
    | 'XCA5'
    | 'BASIC_COATING_MAINTENANCE'
    | 'PERFORMANCE_COATING_MAINTENANCE'
    | 'ULTRA_COAT_MAINTENANCE';
export type OrderTypeEnumValues =
    | 'Accessories'
    | 'Tint'
    | 'Coating'
    | 'PPF'
    | 'Gift'
    | 'MVP'
    | 'Essential'
    | 'Deluxe'
    | 'Ultimate'
    | 'XCA1'
    | 'XCA2'
    | 'XCA3'
    | 'XCA5'
    | 'Basic Coating Maintenance'
    | 'Performance Coating Maintenance'
    | 'Ultra Coat Maintenance';
export enum OrderTypeEnum {
    ACCESSORIES = 'Accessories',
    TINT = 'Tint',
    COATING = 'Coating',
    PPF = 'PPF',
    // GIFT = 'Gift',
    // MVP = 'MVP',
    // ESSENTIAL = 'Essential',
    // DELUXE = 'Deluxe',
    // ULTIMATE = 'Ultimate',
    // XCA1 = 'XCA1',
    // XCA2 = 'XCA2',
    // XCA3 = 'XCA3',
    // XCA5 = 'XCA5',
    // BASIC_COATING_MAINTENANCE = 'Basic Coating Maintenance',
    // PERFORMANCE_COATING_MAINTENANCE = 'Performance Coating Maintenance',
    // ULTRA_COAT_MAINTENANCE = 'Ultra Coat Maintenance',
}

export type OrderModeEnumKeys = 'ALA_CARTE' | 'CONTINUE_LAST_ORDER' | 'PACKAGE';
export type OrderModeEnumValues = 'Ala-carte' | 'Continue Last Order' | 'Package';
export enum OrderModeEnum {
    ALA_CARTE = 'Ala-carte',
    CONTINUE_LAST_ORDER = 'Continue Last Order',
    PACKAGE = 'Package',
}

export type ProductPackageEnumKeys =
    | 'TITAN'
    | 'BRONZE'
    | 'SILVER'
    | 'GOLD'
    | 'PLATINUM'
    | 'ROYAL'
    | 'ROYAL_PLUS'
    | 'ROYAL_PLUS_SAFETY'
    | 'ELEMENTAL'
    | 'ECO_BONZ_9H'
    | 'CRYSTAL_GLOSS_9H'
    | 'MULTI_QUARTZ_9H'
    | 'AVANTGARDE'
    | 'KOSMOS_I'
    | 'KOSMOS_II'
    | 'KOMSOS_III'
    | 'KLEIO'
    | 'MORPHEUS'
    | 'MATTHIAS'
    | 'MAXIMUS';
export type ProductPackageEnumValues =
    | 'Titan'
    | 'Bronze'
    | 'Silver'
    | 'Gold'
    | 'Platinum'
    | 'Royal'
    | 'Royal Plus'
    | 'Royal Plus Safety'
    | 'Elemental'
    | 'Eco Bonz 9H'
    | 'Crystal Gloss 9H'
    | 'Multi Quartz 9H'
    | 'Avantgarde'
    | 'Kosmos I'
    | 'Kosmos II'
    | 'Komsos III'
    | 'Kleio'
    | 'Morpheus'
    | 'Matthias'
    | 'Maximus';
export enum ProductPackageEnum {
    TITAN = 'Titan',
    BRONZE = 'Bronze',
    SILVER = 'Silver',
    GOLD = 'Gold',
    PLATINUM = 'Platinum',
    ROYAL = 'Royal',
    ROYAL_PLUS = 'Royal Plus',
    ROYAL_PLUS_SAFETY = 'Royal Plus Safety',
    ELEMENTAL = 'Elemental',
    ECO_BONZ_9H = 'Eco Bonz 9H',
    CRYSTAL_GLOSS_9H = 'Crystal Gloss 9H',
    MULTI_QUARTZ_9H = 'Multi Quartz 9H',
    AVANTGARDE = 'Avantgarde',
    KOSMOS_I = 'Kosmos I',
    KOSMOS_II = 'Kosmos II',
    KOMSOS_III = 'Komsos III',
    KLEIO = 'Kleio',
    MORPHEUS = 'Morpheus',
    MATTHIAS = 'Matthias',
    MAXIMUS = 'Maximus',
}

interface BaseOrder {
    order_type: OrderTypeEnum;
    order_mode: OrderModeEnum;
    product_package?: ProductPackageEnum;
    is_active: boolean;
}

export interface OrderRequest extends BaseOrder {
    uuid?: string;
    orderitems: OrderItemRequest[];
}

export interface OrderResponse extends BaseOrder {
    uuid: string;
    orderitems: OrderItemResponse[];
}

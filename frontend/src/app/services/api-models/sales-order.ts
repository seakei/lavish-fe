import { GetObjectValueTypes } from 'src/app/utility/get-enum-types';
import { OrderRequest, OrderResponse } from './order';
import { BookingResponse } from './booking';

export const customerRequirementEnum = {
    HIGH_VALUE: 'High Value',
    QUALITY: 'Quality',
    ATTENTION_TO_DETAIL: 'Attention To Detail',
    DEMANDING: 'Demanding',
    EASY: 'Easy',
    SPECIAL_REQUEST: 'Special Request',
};
export type ICustomerRequirementValues = GetObjectValueTypes<typeof customerRequirementEnum>;

export const assignedTeamEnum = {
    TEAM_A: 'Team A',
    TEAM_B: 'Team B',
    TEAM_C: 'Team C',
    TEAM_COATING: 'Coating Team',
};
export type IAssignedTeamValues = GetObjectValueTypes<typeof assignedTeamEnum>;

interface BaseSalesOrder {
    installment_plan: boolean;
    cust_requirement: ICustomerRequirementValues;
    assigned_team: IAssignedTeamValues;
}

export interface SalesOrderRequest extends BaseSalesOrder {
    uuid?: string;
    booking: { uuid: string }; // todo: use booking request?
    orders: OrderRequest[];
}

export interface SalesOrderResponse extends BaseSalesOrder {
    uuid: string;
    number: string;
    booking: BookingResponse;
    orders: OrderResponse[];
    is_active: boolean;
}

// export interface SalesOrder {
//   uuid: string;
//   booking: Booking;
//   orders?: (null)[] | null;
//   cust_requirement: string;
//   assigned_team: string;
//   surcharge_type?: null;
//   discount_type?: null;
//   created_at: string;
//   updated_at: string;
//   is_active: boolean;
//   installment_plan: boolean;
//   duration?: null;
//   surcharge_price: number;
//   upgrade_or_alacarte: boolean;
//   remove_charge: number;
//   sun_visor_charge: number;
//   discount: boolean;
//   discount_amount: number;
//   cust_reference: boolean;
//   reference_fee: number;
//   total_amount: number;
//   balance_amount: number;
//   signature_id: string;
//   number: string;
//   created_by: string;
//   updated_by: string;
//   sales_person_in_charge?: null;
// }
// export interface Booking {
//   uuid: string;
//   created_at: string;
//   updated_at: string;
//   is_active: boolean;
//   booking_date: string;
//   follow_up_date?: null;
//   booking_duration: number;
//   booking_type: number;
//   remark: string;
//   number: string;
//   created_by: string;
//   updated_by: string;
//   vehicle: string;
// }

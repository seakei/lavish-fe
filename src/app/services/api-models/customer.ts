import { BranchEnum } from './_branch';
import { BookingRequest, BookingResponse } from './booking';
import { PartnerRequest, PartnerResponse } from './partner';

interface BaseCustomer {
    car_plate: string;
    car_brand: string;
    branch: BranchEnum;
    package: string;
    remarks: string;
    is_active: boolean;
}

export interface CustomerRequest extends BaseCustomer {
    uuid?: string;
    bookings: BookingRequest[];
    partner: PartnerRequest;
}

export interface CustomerResponse extends BaseCustomer {
    uuid: string;
    bookings: BookingResponse[];
    partner: PartnerResponse;
}

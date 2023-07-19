import { PartnerRequest, PartnerResponse } from './partner';

interface BaseUser {
    username: string;
    // email: string;
    is_active: boolean;
    // created_by?: Date;
    // updated_by?: Date;
}

export interface UserRequest extends BaseUser {
    uuid?: string;
    first_name: string;
    last_name: string;
    password: string;
    partner: PartnerRequest;
}

export interface UserResponse extends BaseUser {
    uuid: string;
    partner: PartnerResponse;
}

import { GetObjectValueTypes } from 'src/app/utility/get-enum-types';
import { BranchEnum } from './_branch';

export const roleEnum = {
    Administrator: 'Administrator',
    Customer: 'Customer',
    'Telemarketer Lead': 'Telemarketer Lead',
    Telemarketer: 'Telemarketer',
    'Indoor Sales Lead': 'Indoor Sales Lead',
    'Indoor Sales': 'Indoor Sales',
    'Technician Lead': 'Technician Lead',
    Technician: 'Technician',
} as const;
export type IRoleValues = GetObjectValueTypes<typeof roleEnum>;

export const profileStatusEnum = {
    NEW: 'New',
    APPOINTMENT: 'Appointment',
    VERIFIED: 'Verified',
    BANNED: 'Banned',
    BLACKLISTED: 'Blacklisted',
} as const;
export type IProfileStatusValues = GetObjectValueTypes<typeof profileStatusEnum>;

interface BasePartner {
    phone_number: string;
    name: string;
    email: string;
    language?: string;
    address?: string;
    customer_from?: string;
    role: IRoleValues;
    branch?: BranchEnum;
    profile_status: IProfileStatusValues;
}

export interface PartnerRequest extends BasePartner {
    uuid?: string;
}

export interface PartnerResponse extends BasePartner {
    uuid: string;
    created_at: string;
    updated_at: string;
}

// export interface Partner {
//     uuid: string;
//     role: string;
//     created_at: string;
//     updated_at: string;
//     is_active: boolean;
//     category: number;
//     profile_status: number;
//     name: string;
//     email: string;
//     ic_number: string;
//     passport_number: string;
//     phone_number: string;
//     customer_from: string;
//     address: string;
//     language: string;
//     created_by?: null;
//     updated_by?: null;
//     user: string;
// }

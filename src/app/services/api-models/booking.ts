import { GetObjectValueTypes } from 'src/app/utility/get-enum-types';

interface BaseBooking {
    is_active: boolean;
    booking_duration: number;
    booking_type: IBookingTypeValues;
    remark: string;
}

export const bookingTypeEnum = {
    APPOINTMENT: 1,
    CLAIM_APPOINTMENT: 2,
    SURVEY_APPOINTMENT: 3,
    BALANCE_APPOINTMENT: 4,
    COATING_MAINTENANCE_APPOINTMENT: 5,
} as const;

export type IBookingTypeValues = GetObjectValueTypes<typeof bookingTypeEnum>;

export const bookingColorsEnum = {
    [bookingTypeEnum.APPOINTMENT]: '#E4C441',
    [bookingTypeEnum.CLAIM_APPOINTMENT]: '#D81B60',
    [bookingTypeEnum.SURVEY_APPOINTMENT]: '#795548',
    [bookingTypeEnum.BALANCE_APPOINTMENT]: '#3F51B5',
    [bookingTypeEnum.COATING_MAINTENANCE_APPOINTMENT]: '#009688',
};

export interface BookingRequest extends BaseBooking {
    uuid?: string;
    booking_date: Date | null;
    follow_up_date: Date | null;
}

export interface BookingResponse extends BaseBooking {
    uuid: string;
    booking_date: string;
    follow_up_date: string | null;
    vehicle: string;
}

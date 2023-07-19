import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { CustomerRequest, CustomerResponse } from './api-models/customer';
import { UserStorageService } from './user-storage.service';
import { UserRequest, UserResponse } from './api-models/user';
import { BookingResponse } from './api-models/booking';
import { SalesOrderRequest, SalesOrderResponse } from './api-models/sales-order';

const baseUrl = 'http://localhost:8000/api';
const authUrl = (path: string) => baseUrl + '/auth-service' + path;
const vehicleUrl = (path: string) => baseUrl + '/vehicle-service' + path;
const usersUrl = (path: string) => baseUrl + '/auth-service/auths' + path;
const bookingUrl = (path: string) => baseUrl + '/vehicle-service/bookings' + path;
const salesOrderUrl = (path: string) => baseUrl + '/salesorder-service/salesorders' + path;

export interface PaginatedResponse<T> {
    count: number;
    results: T[];
}

export interface GetCustomerFilters {
    car_plate: string;
    is_active: string;
}

export interface GetBookingFilters {
    booking_date_after: string;
    booking_date_before: string;
    page_size: string;
}

const removeUnusedItems = (item: { uuid?: string; is_active: boolean }) => {
    // uuid is missing, and not active. means it is just garbage data from frontend
    if (!item.uuid && !item.is_active) {
        return false;
    } else {
        return true;
    }
};

@Injectable({
    providedIn: 'root',
})
export class ApiService {
    constructor(public http: HttpClient, public store: UserStorageService) {}

    // ========================================
    // auth
    // ========================================
    authLogin(username: string, password: string) {
        return this.http.post<{ token: string }>(authUrl('/api-token-auth/'), { username, password });
    }

    authCheck(token: string) {
        return this.http.post<{ token: string }>(authUrl('/api-token-verify/'), { token });
    }

    authUserInfo() {
        return this.http.get<UserResponse>(authUrl('/me/'));
    }

    // ========================================
    // vehicle / customer
    // ========================================
    getCustomers(page: number, filters: Partial<GetCustomerFilters> = {}) {
        const url = new URL(vehicleUrl('/vehicles/'));
        url.searchParams.set('page', `${page}`);
        Object.entries(filters).forEach(([key, value]) => {
            url.searchParams.set(key, value);
        });

        return this.http.get<PaginatedResponse<CustomerResponse>>(url.toString());
    }

    createCustomer(data: CustomerRequest) {
        const url = new URL(vehicleUrl('/vehicles/'));
        data.bookings = data.bookings.filter((book) => book.is_active);
        return this.http.post<CustomerResponse>(url.toString(), data);
    }

    patchCustomer(data: Partial<CustomerRequest>) {
        const url = new URL(vehicleUrl(`/vehicles/${data.uuid}/`));
        delete data.car_plate;

        if (data.bookings) {
            data.bookings = data.bookings.filter(removeUnusedItems);
        }

        return this.http.patch<CustomerResponse>(url.toString(), data);
    }

    getCustomer(uuid: string) {
        const url = new URL(vehicleUrl(`/vehicles/${uuid}/`));
        return this.http.get<CustomerResponse>(url.toString());
    }

    // ========================================
    // user
    // ========================================
    getUsers(page: number) {
        const url = new URL(usersUrl('/'));
        url.searchParams.set('page', `${page}`);
        return this.http.get<PaginatedResponse<UserResponse>>(url.toString());
    }

    createUser(data: UserRequest) {
        const url = new URL(usersUrl('/'));
        delete data.uuid;
        delete data.partner.uuid;
        return this.http.post<UserResponse>(url.toString(), data);
    }

    patchUser(data: Partial<UserRequest>) {
        const url = new URL(usersUrl(`/${data.uuid}/`));
        delete data.password;
        return this.http.patch<UserResponse>(url.toString(), data);
    }

    getUser(uuid: string) {
        const url = new URL(usersUrl(`/${uuid}/`));
        return this.http.get<UserResponse>(url.toString());
    }

    // ========================================
    // bookings
    // ========================================
    getBookings(filters: Partial<GetBookingFilters>) {
        const url = new URL(bookingUrl('/'));
        url.searchParams.set('is_active', 'true');
        url.searchParams.set('page_size', '1000');
        Object.entries(filters).forEach(([key, value]) => {
            url.searchParams.set(key, value);
        });
        return this.http.get<PaginatedResponse<BookingResponse>>(url.toString());
    }

    getBooking(uuid: string) {
        const url = new URL(bookingUrl(`/${uuid}/`));
        return this.http.get<BookingResponse>(url.toString());
    }

    // ========================================
    // sales order
    // ========================================
    createSalesOrder(data: SalesOrderRequest) {
        const url = new URL(salesOrderUrl('/'));
        return this.http.post<SalesOrderResponse>(url.toString(), data);
    }

    getSalesOrder(uuid: string) {
        const url = new URL(salesOrderUrl(`/${uuid}/`));
        return this.http.get<SalesOrderResponse>(url.toString());
    }

    patchSalesOrderWithOrders(data: Partial<SalesOrderRequest>) {
        const url = new URL(salesOrderUrl(`/${data.uuid}/`));

        if (data.orders) {
            data.orders = data.orders.filter(removeUnusedItems).map((order) => ({
                ...order,
                orderitems: order.orderitems.filter(removeUnusedItems),
            }));
        }

        return this.http.patch<SalesOrderResponse>(url.toString(), data);
    }
}

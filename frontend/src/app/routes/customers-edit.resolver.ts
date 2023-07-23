import { inject } from '@angular/core';
import { ResolveFn } from '@angular/router';
import { CustomerResponse } from '../services/api-models/customer';
import { ApiService } from '../services/api.service';
import { of, catchError } from 'rxjs';

export const customerEditResolver: ResolveFn<CustomerResponse | null> = (route) => {
    const api = inject(ApiService);
    const uuid = route.paramMap.get('uuid') || '';

    if (uuid === '') {
        return of(null);
    }

    return api.getCustomer(uuid).pipe(
        catchError((err) => {
            console.error(err);
            return of(null);
        })
    );
};

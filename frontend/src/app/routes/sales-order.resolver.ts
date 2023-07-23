import { ResolveFn } from '@angular/router';
import { SalesOrderResponse } from '../services/api-models/sales-order';
import { inject } from '@angular/core';
import { ApiService } from '../services/api.service';
import { catchError, of } from 'rxjs';

export const salesOrderResolver: ResolveFn<SalesOrderResponse | null> = (route) => {
    const api = inject(ApiService);
    const uuid = route.paramMap.get('uuid') || '';

    if (uuid === '') {
        return of(null);
    }

    return api.getSalesOrder(uuid).pipe(
        catchError((err) => {
            console.error(err);
            return of(null);
        })
    );
};

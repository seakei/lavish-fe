import { inject } from '@angular/core';
import { ResolveFn } from '@angular/router';
import { catchError, of } from 'rxjs';
import { UserResponse } from '../services/api-models/user';
import { ApiService } from '../services/api.service';

export const usersEditResolver: ResolveFn<UserResponse | null> = (route) => {
    const api = inject(ApiService);
    const uuid = route.paramMap.get('uuid') || '';

    if (uuid === '') {
        return of(null);
    }

    return api.getUser(uuid).pipe(
        catchError((err) => {
            console.error(err);
            return of(null);
        })
    );
};

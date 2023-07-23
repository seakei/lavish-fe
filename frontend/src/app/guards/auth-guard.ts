import { inject } from '@angular/core';
import { ActivatedRouteSnapshot, CanActivateFn, Router, RouterStateSnapshot } from '@angular/router';
import { catchError, map, of } from 'rxjs';
import { ApiService } from '../services/api.service';
import { UserStorageService } from '../services/user-storage.service';

export const authGuard: CanActivateFn = (route: ActivatedRouteSnapshot, state: RouterStateSnapshot) => {
    const apiService = inject(ApiService);
    const storeService = inject(UserStorageService);
    const router = inject(Router);
    const token = storeService.getToken();

    const getLoginRoute = (reason: string) =>
        router.createUrlTree(['/auth/login'], { queryParams: { reason, redirect: state.url } });

    if (token !== '') {
        return apiService.authCheck(token).pipe(
            map(() => true),
            catchError(() => {
                storeService.removeToken();
                return of(getLoginRoute('expired'));
            })
        );
    } else {
        return of(getLoginRoute('notoken'));
    }
};

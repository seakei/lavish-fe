import { HttpInterceptorFn } from '@angular/common/http';
import { inject } from '@angular/core';
import { UserStorageService } from './user-storage.service';

export const tokenInterceptor: HttpInterceptorFn = (req, next) => {
    // skip non API URL
    if (!req.url.includes('/api/')) {
        return next(req);
    }

    // skip token API URL
    if (req.url.includes('/api/auth-service/api-token')) {
        return next(req);
    }

    // add auth header
    const store = inject(UserStorageService);
    const authHeaders = req.headers.set('Authorization', `JWT ${store.getToken()}`);
    const authReq = req.clone({ headers: authHeaders });
    return next(authReq);
};

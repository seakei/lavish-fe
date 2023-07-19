import { Injectable } from '@angular/core';
import { UserResponse } from './api-models/user';

const KEYS = {
    LANG: 'user-lang',
    TOKEN: 'user-token',
    USER_DATA: 'user-data',
};

@Injectable({
    providedIn: 'root',
})
export class UserStorageService {
    getLang() {
        return localStorage.getItem(KEYS.LANG) || '';
    }

    setLang(lang: string) {
        localStorage.setItem(KEYS.LANG, lang);
    }

    getToken() {
        return localStorage.getItem(KEYS.TOKEN) || '';
    }

    setToken(token: string) {
        localStorage.setItem(KEYS.TOKEN, token);
    }

    removeToken() {
        localStorage.removeItem(KEYS.TOKEN);
    }

    getData() {
        return JSON.parse(localStorage.getItem(KEYS.USER_DATA) || '{}') as UserResponse;
    }

    setData(user: UserResponse) {
        localStorage.setItem(KEYS.USER_DATA, JSON.stringify(user));
    }
}

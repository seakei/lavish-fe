import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { TranslateLoader } from '@ngx-translate/core';
import { Observable, forkJoin, map, throwError } from 'rxjs';

const validTranslations = ['en', 'zh-CN'];

@Injectable()
export class CustomTranslateLoader implements TranslateLoader {
    constructor(public http: HttpClient) {}

    getTranslation(lang: string): Observable<any> {
        if (validTranslations.includes(lang)) {
            return forkJoin([
                this.http.get<{ [key: string]: any }>(`/assets/i18n/${lang}.json`),
                this.http.get<{ [key: string]: any }>(`/assets/i18n/primeng-${lang}.json`),
            ]).pipe(
                map(([general, primeng]) => ({
                    ...general,
                    primeng,
                }))
            );
        }

        return throwError(() => 'translation file not found');
    }
}

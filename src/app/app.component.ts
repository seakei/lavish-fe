import { Component, OnDestroy, OnInit } from '@angular/core';
import { TranslateService } from '@ngx-translate/core';
import { PrimeNGConfig } from 'primeng/api';
import { Subscription, switchMap, map } from 'rxjs';
import { UserStorageService } from './services/user-storage.service';

@Component({
    selector: 'app-root',
    templateUrl: './app.component.html',
})
export class AppComponent implements OnInit, OnDestroy {
    translationHookSubscription: Subscription;

    constructor(public translate: TranslateService, public config: PrimeNGConfig, public store: UserStorageService) {}

    ngOnInit(): void {
        this.translationHookSubscription = this.translate.onLangChange
            .pipe(
                switchMap((langEvent) =>
                    this.translate
                        .get('primeng')
                        .pipe(map((translations) => ({ translations, currentLang: langEvent.lang })))
                )
            )
            .subscribe(({ translations, currentLang }) => {
                this.config.setTranslation(translations);
                this.store.setLang(currentLang);
            });

        this.translate.setDefaultLang('en');

        if (this.store.getLang() === 'zh-CN') {
            this.translate.use('zh-CN');
        } else {
            this.translate.use('en');
        }
    }

    ngOnDestroy(): void {
        this.translationHookSubscription?.unsubscribe();
    }
}

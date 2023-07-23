import { CommonModule } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { FormsModule, NonNullableFormBuilder, ReactiveFormsModule, Validators } from '@angular/forms';
import { ActivatedRoute, Router, RouterModule } from '@angular/router';
import { TranslateModule, TranslateService } from '@ngx-translate/core';
import { Message } from 'primeng/api';
import { finalize, map, switchMap, tap } from 'rxjs';
import { LanguageSelectionComponent } from 'src/app/components/language-selection/language-selection.component';
import { CustomPrimengModule } from 'src/app/modules/custom-primeng.module';
import { ApiService } from 'src/app/services/api.service';
import { UserStorageService } from 'src/app/services/user-storage.service';

@Component({
    selector: 'app-login',
    standalone: true,
    imports: [
        CommonModule,
        FormsModule,
        ReactiveFormsModule,
        CustomPrimengModule,
        TranslateModule,
        RouterModule,
        LanguageSelectionComponent,
    ],
    templateUrl: './login.component.html',
})
export class LoginComponent implements OnInit {
    loading = false;
    loginErrorMessage: Message[] = [];

    form = this.fb.group({
        user: this.fb.control('', [Validators.required]),
        pass: this.fb.control('', [Validators.required]),
    });

    constructor(
        public fb: NonNullableFormBuilder,
        public translate: TranslateService,
        public apiService: ApiService,
        public router: Router,
        public activatedRoute: ActivatedRoute,
        public store: UserStorageService
    ) {}

    ngOnInit(): void {
        const reason = this.activatedRoute.snapshot.queryParamMap.get('reason') || '';
        const reasonMap: { [key: string]: string } = {
            expired: 'error_login_token_expired',
            notoken: 'error_login_token_notoken',
        };

        if (reason in reasonMap) {
            this.translate.get(reasonMap[reason]).subscribe((detail) => {
                this.loginErrorMessage = [
                    {
                        closable: true,
                        severity: 'error',
                        detail,
                    },
                ];
            });
        }
    }

    handleLogin() {
        this.loginErrorMessage = [];

        if (this.form.invalid || this.loading) {
            return;
        }

        this.loading = true;
        this.apiService
            .authLogin(this.form.controls.user.value, this.form.controls.pass.value)
            .pipe(
                tap((res) => {
                    this.store.setToken(res.token);
                }),
                switchMap(() => {
                    return this.apiService.authUserInfo();
                }),
                finalize(() => (this.loading = false))
            )
            .subscribe({
                next: (user) => {
                    this.store.setData(user);

                    const redirect = this.activatedRoute.snapshot.queryParamMap.get('redirect');
                    if (redirect) {
                        this.router.navigateByUrl(redirect);
                    } else {
                        this.router.navigate(['/dashboard/home']);
                    }
                },
                error: () => {
                    this.loginErrorMessage = [
                        {
                            closable: true,
                            severity: 'error',
                            detail: this.translate.instant('error_invalid_login'),
                        },
                    ];
                },
            });
    }
}

import { CommonModule } from '@angular/common';
import { ChangeDetectionStrategy, Component, OnInit } from '@angular/core';
import { NonNullableFormBuilder, ReactiveFormsModule, Validators } from '@angular/forms';
import { ActivatedRoute, Router, RouterModule } from '@angular/router';
import { TranslateModule, TranslateService } from '@ngx-translate/core';
import { MessageService } from 'primeng/api';
import { defer } from 'rxjs';
import { BackClickDirective } from 'src/app/components/back-click/back-click.directive';
import { CustomPrimengModule } from 'src/app/modules/custom-primeng.module';
import { BranchEnum, branches } from 'src/app/services/api-models/_branch';
import { IProfileStatusValues, IRoleValues, profileStatusEnum, roleEnum } from 'src/app/services/api-models/partner';
import { UserResponse } from 'src/app/services/api-models/user';
import { ApiService } from 'src/app/services/api.service';
import { enumToOptions } from 'src/app/utility/enum-to-options';

const roleOptions = enumToOptions(roleEnum, 'role_option').filter((opt) => opt.value !== roleEnum.Customer);
const profileStatusOptions = enumToOptions(profileStatusEnum, 'profile_status_option');

@Component({
    selector: 'app-users-create',
    standalone: true,
    imports: [
        CommonModule,
        CustomPrimengModule,
        TranslateModule,
        ReactiveFormsModule,
        BackClickDirective,
        RouterModule,
    ],
    templateUrl: './users-create.component.html',
    changeDetection: ChangeDetectionStrategy.OnPush,
})
export class UsersCreateComponent implements OnInit {
    roleOptions = roleOptions;
    branchOptions = branches;
    profileStatusOptions = profileStatusOptions;

    form = this.fb.group({
        uuid: this.fb.control(''),
        username: this.fb.control('', [Validators.required]),
        password: this.fb.control('', [Validators.minLength(8)]),
        first_name: this.fb.control(''),
        last_name: this.fb.control(''),
        is_active: this.fb.control(true),
        partner: this.fb.group({
            uuid: this.fb.control(''),
            name: this.fb.control('', [Validators.required]),
            email: this.fb.control('', [Validators.required, Validators.email]),
            role: this.fb.control<IRoleValues>(roleEnum['Indoor Sales']),
            phone_number: this.fb.control('', [Validators.required]),
            branch: this.fb.control(BranchEnum.PUCHONG),
            profile_status: this.fb.control<IProfileStatusValues>(profileStatusEnum.NEW),
        }),
    });

    constructor(
        public fb: NonNullableFormBuilder,
        public api: ApiService,
        public router: Router,
        public msg: MessageService,
        public translate: TranslateService,
        public activatedRoute: ActivatedRoute
    ) {}

    ngOnInit(): void {
        const existingUser: UserResponse = this.activatedRoute.snapshot.data['existingUser'];
        if (existingUser) {
            const { partner, ...restUser } = existingUser;

            this.form.patchValue(restUser);
            this.form.controls.username.disable();
            this.form.controls.password.disable();
            if (partner) {
                this.form.controls.partner.patchValue(partner);
            }
        }
    }

    save() {
        if (this.form.invalid) {
            return;
        }

        const value = this.form.getRawValue();
        defer(() => {
            if (value.uuid === '') {
                return this.api.createUser(value);
            }

            return this.api.patchUser(value);
        }).subscribe({
            next: () => {
                this.router.navigate(['/dashboard/users']);
            },
            error: (err) => {
                console.error(err);

                const errors: any = err.error;
                if (errors?.partner?.email) {
                    this.form.get('partner.email')!.setErrors({ email: true });
                }

                const summary = 'error_on_form';
                let detail = 'error_on_form_server';

                this.msg.add({
                    severity: 'error',
                    summary: this.translate.instant(summary),
                    detail: this.translate.instant(detail),
                    life: 5000,
                });
            },
        });
    }
}

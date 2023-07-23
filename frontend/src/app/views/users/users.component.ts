import { CommonModule } from '@angular/common';
import { ChangeDetectionStrategy, Component, OnInit } from '@angular/core';
import { TranslateModule } from '@ngx-translate/core';
import { LazyLoadEvent } from 'primeng/api';
import { BehaviorSubject, Observable, filter, finalize, map, switchMap, tap } from 'rxjs';
import { CustomPrimengModule } from 'src/app/modules/custom-primeng.module';
import { UserResponse } from 'src/app/services/api-models/user';
import { ApiService, PaginatedResponse } from 'src/app/services/api.service';

@Component({
    selector: 'app-users',
    standalone: true,
    imports: [CommonModule, CustomPrimengModule, TranslateModule],
    templateUrl: './users.component.html',
    changeDetection: ChangeDetectionStrategy.OnPush,
})
export class UsersComponent implements OnInit {
    isLoading = false;
    tableTrigger$ = new BehaviorSubject<LazyLoadEvent>({});
    userList$: Observable<PaginatedResponse<UserResponse>>;

    constructor(public api: ApiService) {}

    ngOnInit(): void {
        this.userList$ = this.tableTrigger$.pipe(
            filter((data) => Object.keys(data).length > 0),
            tap(() => (this.isLoading = true)),
            switchMap((table) => {
                const page = table.first! / table.rows! + 1;
                return this.api.getUsers(page).pipe(finalize(() => (this.isLoading = false)));
            }),
            map((data) => {
                return {
                    ...data,
                    results: data.results.map((user) => ({
                        ...user,
                        partner: user.partner || {},
                    })),
                };
            })
        );
    }

    deleteUser(uuid: string) {
        this.api.patchUser({ uuid, is_active: false }).subscribe(() => {
            this.tableTrigger$.next(this.tableTrigger$.value);
        });
    }
}

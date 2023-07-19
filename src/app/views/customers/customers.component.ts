import { CommonModule } from '@angular/common';
import { HttpClientModule } from '@angular/common/http';
import { ChangeDetectionStrategy, Component, OnInit } from '@angular/core';
import { RouterModule } from '@angular/router';
import { TranslateModule } from '@ngx-translate/core';
import { LazyLoadEvent } from 'primeng/api';
import { BehaviorSubject, Observable, filter, finalize, switchMap, tap } from 'rxjs';
import { CustomPrimengModule } from 'src/app/modules/custom-primeng.module';
import { CustomerResponse } from 'src/app/services/api-models/customer';
import { ApiService, PaginatedResponse } from 'src/app/services/api.service';

@Component({
    selector: 'app-customers',
    standalone: true,
    imports: [CommonModule, CustomPrimengModule, RouterModule, HttpClientModule, TranslateModule],
    templateUrl: './customers.component.html',
    changeDetection: ChangeDetectionStrategy.OnPush,
})
export class CustomersComponent implements OnInit {
    isLoading = true;
    customers$: Observable<PaginatedResponse<CustomerResponse>>;
    tableTrigger$ = new BehaviorSubject<LazyLoadEvent>({});

    constructor(public api: ApiService) {}

    ngOnInit(): void {
        this.customers$ = this.tableTrigger$.asObservable().pipe(
            filter((data) => Object.keys(data).length > 0),
            tap(() => (this.isLoading = true)),
            switchMap((data) => {
                const page = data.first! / data.rows! + 1;
                return this.api
                    .getCustomers(page, { is_active: 'true' })
                    .pipe(finalize(() => (this.isLoading = false)));
            })
        );
    }

    deleteCustomer(uuid: string) {
        this.api.patchCustomer({ uuid, is_active: false }).subscribe(() => {
            this.tableTrigger$.next(this.tableTrigger$.value);
        });
    }

    // handleChange(table: Table, filterName: string, targ: EventTarget | null) {
    //     table.filter((targ as HTMLInputElement).value, filterName, 'contains');
    // }
}

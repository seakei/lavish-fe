import { CommonModule } from '@angular/common';
import { ChangeDetectionStrategy, Component } from '@angular/core';
import { NonNullableFormBuilder, ReactiveFormsModule } from '@angular/forms';
import { ActivatedRoute, Router, RouterModule } from '@angular/router';
import { TranslateModule, TranslateService } from '@ngx-translate/core';
import { CustomPrimengModule } from 'src/app/modules/custom-primeng.module';
import { SalesOrderResponse } from 'src/app/services/api-models/sales-order';
import { ApiService } from 'src/app/services/api.service';

@Component({
    selector: 'app-sales-order-create-summary',
    standalone: true,
    imports: [CommonModule, CustomPrimengModule, ReactiveFormsModule, TranslateModule, RouterModule],
    templateUrl: './sales-order-create-summary.component.html',
    changeDetection: ChangeDetectionStrategy.OnPush,
})
export class SalesOrderCreateSummaryComponent {
    salesOrder: SalesOrderResponse = this.activatedRoute.snapshot.data['existingSalesOrder'];

    constructor(
        public fb: NonNullableFormBuilder,
        public activatedRoute: ActivatedRoute,
        public translate: TranslateService,
        public api: ApiService,
        public router: Router
    ) {}
}

import { CommonModule } from '@angular/common';
import { ChangeDetectionStrategy, Component, OnInit } from '@angular/core';
import { NavigationEnd, Router, RouterModule } from '@angular/router';
import { TranslateModule, TranslateService } from '@ngx-translate/core';
import { filter, map, startWith } from 'rxjs';
import { BackClickDirective } from 'src/app/components/back-click/back-click.directive';
import { CustomPrimengModule } from 'src/app/modules/custom-primeng.module';

const labels = ['details', 'orders', 'summary'];

@Component({
    selector: 'app-sales-order-create',
    standalone: true,
    imports: [CommonModule, CustomPrimengModule, BackClickDirective, TranslateModule, RouterModule],
    templateUrl: './sales-order-create.component.html',
    changeDetection: ChangeDetectionStrategy.OnPush,
})
export class SalesOrderCreateComponent implements OnInit {
    stepper: { label: string }[] = [];

    currentPageIndex$ = this.router.events.pipe(
        filter((evt) => evt instanceof NavigationEnd),
        map((evt) => (evt as NavigationEnd).url),
        startWith(this.router.url),
        map((url) => url.replace('/dashboard/sales-order/create', '')),
        map((url) => labels.findIndex((label) => url.startsWith(`/${label}`)))
    );

    constructor(public translate: TranslateService, public router: Router) {}

    ngOnInit(): void {
        const stepperLabels = labels.map((label) => `sales_order.${label}`);

        this.translate.get(stepperLabels).subscribe((data) => {
            this.stepper = stepperLabels.map((label) => data[label]).map((label: string) => ({ label }));
        });
    }
}

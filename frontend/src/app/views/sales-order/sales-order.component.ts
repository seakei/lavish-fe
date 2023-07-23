import { ChangeDetectionStrategy, Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { CustomPrimengModule } from 'src/app/modules/custom-primeng.module';
import { TranslateModule } from '@ngx-translate/core';

@Component({
    selector: 'app-sales-order',
    standalone: true,
    imports: [CommonModule, CustomPrimengModule, TranslateModule],
    templateUrl: './sales-order.component.html',
    changeDetection: ChangeDetectionStrategy.OnPush,
})
export class SalesOrderComponent {}

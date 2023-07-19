import { Routes } from '@angular/router';
import { SalesOrderCreateDetailsComponent } from '../views/sales-order-create-details/sales-order-create-details.component';
import { SalesOrderCreateOrderComponent } from '../views/sales-order-create-order/sales-order-create-order.component';
import { SalesOrderCreateSummaryComponent } from '../views/sales-order-create-summary/sales-order-create-summary.component';
import { SalesOrderCreateComponent } from '../views/sales-order-create/sales-order-create.component';
import { SalesOrderComponent } from '../views/sales-order/sales-order.component';
import { salesOrderResolver } from './sales-order.resolver';

export const routes: Routes = [
    {
        path: '',
        component: SalesOrderComponent,
    },
    {
        path: 'create',
        component: SalesOrderCreateComponent,
        children: [
            {
                path: 'details',
                component: SalesOrderCreateDetailsComponent,
            },
            {
                path: 'orders/:uuid',
                component: SalesOrderCreateOrderComponent,
                resolve: {
                    existingSalesOrder: salesOrderResolver,
                },
            },
            {
                path: 'summary/:uuid',
                component: SalesOrderCreateSummaryComponent,
                resolve: {
                    existingSalesOrder: salesOrderResolver,
                },
            },
        ],
    },
];

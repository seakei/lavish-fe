import { Routes } from '@angular/router';
import { CustomersCreateComponent } from '../views/customers-create/customers-create.component';
import { CustomersComponent } from '../views/customers/customers.component';
import { DashboardComponent } from '../views/dashboard/dashboard.component';
import { SettingsComponent } from '../views/settings/settings.component';
import { TodayCalendarComponent } from '../views/today-calendar/today-calendar.component';
import { UsersCreateComponent } from '../views/users-create/users-create.component';
import { UsersComponent } from '../views/users/users.component';
import { customerEditResolver } from './customers-edit.resolver';
import { usersEditResolver } from './users-edit.resolver';

export const routes: Routes = [
    {
        path: '',
        component: DashboardComponent,
        children: [
            {
                path: 'home',
                component: TodayCalendarComponent,
            },
            {
                path: 'customers',
                component: CustomersComponent,
            },
            {
                path: 'customers/create',
                component: CustomersCreateComponent,
            },
            {
                path: 'customers/edit/:uuid',
                component: CustomersCreateComponent,
                resolve: {
                    existingCustomer: customerEditResolver,
                },
            },
            {
                path: 'sales-order',
                loadChildren: () => import('./dashboard-sales-order.route').then((mod) => mod.routes),
            },
            {
                path: 'users',
                component: UsersComponent,
            },
            {
                path: 'users/create',
                component: UsersCreateComponent,
            },
            {
                path: 'users/edit/:uuid',
                component: UsersCreateComponent,
                resolve: {
                    existingUser: usersEditResolver,
                },
            },
            {
                path: 'settings',
                component: SettingsComponent,
            },
        ],
    },
];

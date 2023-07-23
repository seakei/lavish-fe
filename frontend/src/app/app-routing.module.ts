import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
// import { authGuard } from './guards/auth-guard';

const routes: Routes = [
    {
        path: 'dashboard',
        loadChildren: () => import('./routes/dashboard.route').then((m) => m.routes),
        // canActivate: [authGuard],
    },
    {
        path: 'auth',
        children: [
            {
                path: 'login',
                loadComponent: () => import('./views/login/login.component').then((m) => m.LoginComponent),
            },
        ],
    },
    { path: '', redirectTo: '/auth/login', pathMatch: 'full' },
];

@NgModule({
    imports: [RouterModule.forRoot(routes, { useHash: true, scrollPositionRestoration: 'top' })],
    exports: [RouterModule],
})
export class AppRoutingModule {}

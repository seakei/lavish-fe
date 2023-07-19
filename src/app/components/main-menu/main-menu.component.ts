import { ChangeDetectionStrategy, Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { TranslateModule } from '@ngx-translate/core';
import { RouterModule } from '@angular/router';
import { UserStorageService } from 'src/app/services/user-storage.service';
import { roleEnum } from 'src/app/services/api-models/partner';

@Component({
    selector: 'app-main-menu',
    standalone: true,
    imports: [CommonModule, TranslateModule, RouterModule],
    templateUrl: './main-menu.component.html',
    changeDetection: ChangeDetectionStrategy.OnPush,
})
export class MainMenuComponent implements OnInit {
    items = [
        {
            icon: 'pi-home',
            text: 'home',
            link: ['/dashboard/home'],
        },
        {
            icon: 'pi-users',
            text: 'customers',
            link: ['/dashboard/customers'],
        },
        {
            icon: 'pi-folder-open',
            text: 'sales_order.label',
            link: ['/dashboard/sales-order'],
        },
        {
            icon: 'pi-user-edit',
            text: 'users',
            link: ['/dashboard/users'],
        },
        {
            icon: 'pi-cog',
            text: 'settings',
            link: ['/dashboard/settings'],
        },
    ];

    constructor(public store: UserStorageService) {}

    ngOnInit(): void {
        const role = this.store.getData().partner.role;
        if (role !== roleEnum.Administrator) {
            this.items = this.items.filter((item) => item.text !== 'users');
        }
    }
}

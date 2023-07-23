import { ChangeDetectionStrategy, Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { TranslateModule } from '@ngx-translate/core';
import { RouterModule } from '@angular/router';
import { UserStorageService } from 'src/app/services/user-storage.service';

@Component({
    selector: 'app-top-bar',
    standalone: true,
    imports: [CommonModule, TranslateModule, RouterModule],
    templateUrl: './top-bar.component.html',
    styles: [],
    changeDetection: ChangeDetectionStrategy.OnPush,
})
export class TopBarComponent {
    name: string;

    constructor(public store: UserStorageService) {}

    ngOnInit(): void {
        this.name = this.store.getData().partner.name;
    }
}

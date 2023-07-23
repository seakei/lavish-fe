import { ChangeDetectionStrategy, Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { MainMenuComponent } from 'src/app/components/main-menu/main-menu.component';
import { TopBarComponent } from 'src/app/components/top-bar/top-bar.component';
import { RouterModule } from '@angular/router';
import { EventsCalendarComponent } from 'src/app/components/events-calendar/events-calendar.component';

@Component({
    selector: 'app-dashboard',
    standalone: true,
    imports: [CommonModule, TopBarComponent, MainMenuComponent, RouterModule, EventsCalendarComponent],
    templateUrl: './dashboard.component.html',
    changeDetection: ChangeDetectionStrategy.OnPush,
})
export class DashboardComponent {}

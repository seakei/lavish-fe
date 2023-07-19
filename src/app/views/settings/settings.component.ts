import { ChangeDetectionStrategy, Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { TranslateModule } from '@ngx-translate/core';
import { LanguageSelectionComponent } from 'src/app/components/language-selection/language-selection.component';
import { CustomPrimengModule } from 'src/app/modules/custom-primeng.module';
import { BackClickDirective } from 'src/app/components/back-click/back-click.directive';

@Component({
    selector: 'app-settings',
    standalone: true,
    imports: [CommonModule, TranslateModule, LanguageSelectionComponent, CustomPrimengModule, BackClickDirective],
    templateUrl: './settings.component.html',
    changeDetection: ChangeDetectionStrategy.OnPush,
})
export class SettingsComponent {}

import { ChangeDetectionStrategy, Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { TranslateModule, TranslateService } from '@ngx-translate/core';
import { map, startWith } from 'rxjs';
import { CustomPrimengModule } from 'src/app/modules/custom-primeng.module';

@Component({
    selector: 'app-language-selection',
    standalone: true,
    imports: [CommonModule, TranslateModule, CustomPrimengModule],
    templateUrl: './language-selection.component.html',
    changeDetection: ChangeDetectionStrategy.OnPush,
})
export class LanguageSelectionComponent {
    activeLang$ = this.translate.onLangChange.pipe(
        map((langChange) => langChange.lang),
        startWith(this.translate.currentLang)
    );

    constructor(public translate: TranslateService) {}

    changeLang(lang: string) {
        this.translate.use(lang);
    }
}

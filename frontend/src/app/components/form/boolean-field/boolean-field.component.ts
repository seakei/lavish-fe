import { CommonModule } from '@angular/common';
import { ChangeDetectionStrategy, Component, Input } from '@angular/core';
import { ReactiveFormsModule } from '@angular/forms';
import { TranslateModule } from '@ngx-translate/core';
import { CustomPrimengModule } from 'src/app/modules/custom-primeng.module';

@Component({
    selector: 'app-boolean-field',
    standalone: true,
    imports: [CommonModule, TranslateModule, ReactiveFormsModule, CustomPrimengModule],
    templateUrl: './boolean-field.component.html',
    changeDetection: ChangeDetectionStrategy.OnPush,
})
export class BooleanFieldComponent {
    @Input() formGroupPass: any;
    @Input() formControlNamePass: string;
    @Input() label = 'Question?';
    @Input() inputId = 'temp-id';

    @Input() yesText = 'general_yes_option';
    @Input() noText = 'general_no_option';
}

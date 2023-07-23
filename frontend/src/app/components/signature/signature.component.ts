import { ChangeDetectionStrategy, Component, ElementRef, HostListener, OnInit, ViewChild } from '@angular/core';
import { CommonModule } from '@angular/common';
import { CustomPrimengModule } from 'src/app/modules/custom-primeng.module';
import SignaturePad from 'signature_pad';
import { TranslateModule } from '@ngx-translate/core';

@Component({
    selector: 'app-signature',
    standalone: true,
    imports: [CommonModule, CustomPrimengModule, TranslateModule],
    templateUrl: './signature.component.html',
    changeDetection: ChangeDetectionStrategy.OnPush,
})
export class SignatureComponent implements OnInit {
    @ViewChild('canvas', { static: true })
    canvas: ElementRef<HTMLCanvasElement>;

    public signature: SignaturePad;

    ngOnInit(): void {
        this.signature = new SignaturePad(this.canvas.nativeElement);
    }
}

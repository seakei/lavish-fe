import { Location } from '@angular/common';
import { Directive, HostListener } from '@angular/core';
import { Router } from '@angular/router';

@Directive({
    selector: '[backClick]',
    standalone: true,
})
export class BackClickDirective {
    constructor(public location: Location, public router: Router) {}

    @HostListener('click')
    onClick() {
        if (history.length > 0) {
            this.location.back();
        } else {
            this.router.navigate(['/']);
        }

        return false;
    }
}

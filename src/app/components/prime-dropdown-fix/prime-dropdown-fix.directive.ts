import { AfterViewInit, Directive, ElementRef, Host, Optional } from '@angular/core';
import { Dropdown } from 'primeng/dropdown';

@Directive({
    selector: '[pDropdownFix]',
    standalone: true,
})
export class PrimeDropdownFixDirective implements AfterViewInit {
    constructor(public el: ElementRef, @Host() @Optional() public dropdown: Dropdown) {}

    ngAfterViewInit(): void {
        if (!this.dropdown) {
            return;
        }

        (this.dropdown.filterBy as any) = {
            split: (_: any) => [(item: any) => item],
        };
    }
}

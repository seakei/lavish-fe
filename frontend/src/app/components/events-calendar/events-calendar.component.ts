import { BreakpointObserver } from '@angular/cdk/layout';
import { CommonModule } from '@angular/common';
import { ChangeDetectionStrategy, Component, OnInit } from '@angular/core';
// import { CalendarEvent, CalendarModule } from 'angular-calendar';
import { Observable, map, debounceTime } from 'rxjs';
import { CustomPrimengModule } from 'src/app/modules/custom-primeng.module';

const getFakeEvents = () => {
    const today = new Date();
};

@Component({
    selector: 'app-events-calendar',
    standalone: true,
    imports: [CommonModule, CustomPrimengModule],
    templateUrl: './events-calendar.component.html',
    changeDetection: ChangeDetectionStrategy.OnPush,
})
export class EventsCalendarComponent implements OnInit {
    numOfDays$: Observable<number>;
    viewDate = new Date();

    // events: CalendarEvent[] = [
    //     {
    //         start: new Date(),
    //         title: 'Sample event',
    //     },
    // ];

    constructor(public bpo: BreakpointObserver) {}

    ngOnInit(): void {
        // const bpToDaysMap: Record<string, number> = {
        //     '(min-width: 640px)': 1,
        //     '(min-width: 768px)': 3,
        //     '(min-width: 1024px)': 3,
        //     '(min-width: 1280px)': 5,
        //     '(min-width: 1536px)': 5,
        // };
        // this.numOfDays$ = this.bpo.observe(Object.keys(bpToDaysMap)).pipe(
        //     debounceTime(200),
        //     map((state) => {
        //         const matches = Object.keys(state.breakpoints).filter((key) => !!state.breakpoints[key]);
        //         if (matches.length === 0) {
        //             return 1;
        //         }
        //         return Math.max(...matches.map((key) => bpToDaysMap[key]));
        //     })
        // );
    }

    // eventClicked({ event }: { event: CalendarEvent }) {
    //     alert(`Clicked on event "${event.title}"`);
    //     console.log(event);
    // }
}

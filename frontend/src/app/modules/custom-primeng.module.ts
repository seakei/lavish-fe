import { NgModule } from '@angular/core';
import { AccordionModule } from 'primeng/accordion';
import { MessageService } from 'primeng/api';
import { ButtonModule } from 'primeng/button';
import { CalendarModule } from 'primeng/calendar';
import { CardModule } from 'primeng/card';
import { DropdownModule } from 'primeng/dropdown';
import { DynamicDialogModule } from 'primeng/dynamicdialog';
import { FieldsetModule } from 'primeng/fieldset';
import { InputNumberModule } from 'primeng/inputnumber';
import { InputTextModule } from 'primeng/inputtext';
import { InputTextareaModule } from 'primeng/inputtextarea';
import { MenuModule } from 'primeng/menu';
import { MessagesModule } from 'primeng/messages';
import { MultiSelectModule } from 'primeng/multiselect';
import { PaginatorModule } from 'primeng/paginator';
import { PanelModule } from 'primeng/panel';
import { PasswordModule } from 'primeng/password';
import { RadioButtonModule } from 'primeng/radiobutton';
import { StepsModule } from 'primeng/steps';
import { TableModule } from 'primeng/table';
import { ToastModule } from 'primeng/toast';

@NgModule({
    imports: [
        ButtonModule,
        InputTextModule,
        PasswordModule,
        MessagesModule,
        TableModule,
        CardModule,
        DropdownModule,
        MenuModule,
        PaginatorModule,
        CalendarModule,
        RadioButtonModule,
        InputTextareaModule,
        InputNumberModule,
        ToastModule,
        PanelModule,
        DynamicDialogModule,
        MultiSelectModule,
        StepsModule,
        AccordionModule,
        FieldsetModule,
    ],
    exports: [
        ButtonModule,
        InputTextModule,
        PasswordModule,
        MessagesModule,
        TableModule,
        CardModule,
        DropdownModule,
        MenuModule,
        PaginatorModule,
        CalendarModule,
        RadioButtonModule,
        InputTextareaModule,
        InputNumberModule,
        ToastModule,
        PanelModule,
        DynamicDialogModule,
        MultiSelectModule,
        StepsModule,
        AccordionModule,
        FieldsetModule,
    ],
    providers: [MessageService],
})
export class CustomPrimengModule {}

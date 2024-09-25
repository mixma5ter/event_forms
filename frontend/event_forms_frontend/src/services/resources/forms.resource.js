import { CrudService } from "@/services/api/crud.service";

export class FormsResource extends CrudService {
    constructor() {
        super("forms/");
    }

    getForms() {
        return this.get();
    }

    createForm(form) {
        return this.post(form);
    }
}
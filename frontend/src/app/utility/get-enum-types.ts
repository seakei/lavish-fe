export type GetObjectKeyTypes<T> = keyof T;
export type GetObjectValueTypes<T> = T[GetObjectKeyTypes<T>];

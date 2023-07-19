interface EnumOptions<T> {
    label: string;
    value: T;
}

export function enumToOptions<T>(inputEnum: { [key: string]: T }, prefix: string): EnumOptions<T>[] {
    return Object.entries(inputEnum).map(([label, value]) => ({
        label: prefix === '' ? `${value}` : `${prefix}.${label}`,
        value,
    }));
}

export function getEnumKeyFromValue<T>(inputEnum: { [key: string]: T }, searchVal: T): string {
    return Object.keys(inputEnum).find((key) => inputEnum[key] === searchVal)!;
}

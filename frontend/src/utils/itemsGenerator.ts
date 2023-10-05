class ItemsGeneratorClass {
    private names: string[] = ['Mercedes Benz AMD', 'Schoda', 'Deng deng'];
    private cities: string[] = ['Almaty', 'Astana', 'Shymkent'];

    generateItem(): any {
        return {
            name: this.getRandomInd(this.names),
            price: Math.floor(Math.random() * 10000000),
            city: this.getRandomInd(this.cities),
        }
    }
    getRandomInd(array: string[]): string | null {
        return array.length <= 0 ? null : array[Math.floor(Math.random() * array.length)];
    }
}


const ItemsGenerator = new ItemsGeneratorClass();

export default ItemsGenerator;
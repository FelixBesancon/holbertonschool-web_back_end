export default function updateUniqueItems (map) {
  if (!(map instanceof Map)) throw new Error('Cannot process');
  map.forEach((number, item) => {
    if (number === 1) map.set(item, 100);
  });
}

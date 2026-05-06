export default function cleanSet (set, startString) {
  if (!startString) return '';
  return Array
    .from(set)
    .filter(string => string.startsWith(startString))
    .map(string => string.slice(startString.length))
    .join('-');
}

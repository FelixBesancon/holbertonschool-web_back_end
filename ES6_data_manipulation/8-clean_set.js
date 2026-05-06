export default function cleanSet (set, startString) {
  return startString === ''
    ? ''
    : (
        Array
          .from(set)
          .filter(string => string.startsWith(startString))
          .map(string => string.slice(startString.length))
          .join('-')
      );
}

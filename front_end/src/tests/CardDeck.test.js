import CardDeck from './../CardDeck';

test('CardDeck renders div named CardDeckApp', () => {
  const deck = CardDeck({"user_type": "followers"});

  expect(deck.type).toBe('div');
  expect(deck.props['className']).toBe('CardDeckApp');
});

function setup() {
  return 4;
}

describe('4 = 4', () => {
  it('4 should equal 4 duh', () => {
    const x = setup();
    expect(x).toBe(4);
  });
});
"""
Author: Raphael Gonzalez (RAffA)
"""
import unittest as ut
from pathlib import Path
from hspiceParser import *
# pickle was imported via the hspiceParser

class TestTransBin9601(ut.TestCase):
    """
    this tests the functions for getting to the dictionary structure for the 9601 format of a transient analysis.
    """
    def setUp(self) -> None:
        self.dir = Path(__file__).parent.resolve()
        self.path = self.dir/'test_9601.tr0'

    def test_is_binary(self):
        self.assertTrue(is_binary(self.path))

    def test_get_from_ext(self):
        self.assertEqual(get_from_ext(self.path), 'tr')

    def test_read_binary_signal_file(self):
        """
        the function that is being tested is dependant on read_data_block
        :return:
        """
        header_str, data_blocks = read_binary_signal_file(self.path)
        self.assertTrue(header_str == "00050000000000009601    * rccircuit.sp                                                  06/05/2020      15:06:55 Copyright (c) 1986 - 2020 by Synopsys, Inc. All Rights Reserved.          0                                                                              1       1       1       1       8     TIME            v(0             v(vo            v(vs            i(vs            $&%#    ")

        with open(self.dir/'data_blocks_9601.pickle', 'rb') as f:
            truth_blocks = pickle.load(f)
            self.assertTrue(data_blocks == truth_blocks)

    def test_parse_header(self):
        """
        the function that is being tested is dependant on parse_var_name and get_var_index
        :return:
        """
        header_str, _ = read_binary_signal_file(self.path)
        var_count, parsed_header = parse_header(header_str)
        self.assertEqual(parsed_header, ['TIME', 'v_0', 'v_vo', 'v_vs', 'i_vs'])
        self.assertEqual(5, var_count)

    def test_break_by_sweep(self):
        _, data_lst = read_binary_signal_file(self.path)
        data_lst = sum(data_lst, [])
        sweep_lst = break_by_sweep(data_lst, '9601')
        with open(self.dir/'sweep_lst_9601.pickle', 'rb') as f:
            truth_blocks = pickle.load(f)
            self.assertTrue(sweep_lst == truth_blocks)

        self.assertTrue(len(sweep_lst) == 1)

    def test_general_make_dict(self):
        header_str, data_lst = read_binary_signal_file(self.path)
        sweep_lst = break_by_sweep(sum(data_lst, []), '9601')
        _, var_lst = parse_header(header_str)
        data_dict, _, _, _ = general_make_dict(var_lst, sweep_lst, header_str, False)  # the test file has no sweeps (break by sweep still has a purpose though
        with open(self.dir/'data_dict_9601.pickle', 'rb') as f:
            truth_dict = pickle.load(f)
            self.assertEqual(data_dict, truth_dict)

    def test_write_to_dict(self):
        header_str, data_lst = read_binary_signal_file(self.path)
        data_dict, _, _, _ = write_to_dict(data_lst, header_str, 'tr')
        with open(self.dir/'data_dict_9601.pickle', 'rb') as f:
            truth_dict = pickle.load(f)
            self.assertEqual(data_dict, truth_dict)

class TestACBin9601(ut.TestCase):
    """
    this tests the functions for getting to the dictionary structure for the 9601 format
    """
    def setUp(self) -> None:
        self.dir = Path(__file__).parent.resolve()
        self.path = self.dir/'test_9601.ac0'

    def test_is_binary(self):
        self.assertTrue(is_binary(self.path))

    def test_get_from_ext(self):
        self.assertEqual(get_from_ext(self.path), 'ac')

    def test_read_binary_signal_file(self):
        """
        the function that is being tested is dependant on read_data_block
        :return:
        """
        header_str, data_blocks = read_binary_signal_file(self.path)
        self.assertEqual(header_str, "00050000000000009601    * rccircuit.sp                                                  04/23/2021      19:22:51 Copyright (c) 1986 - 2021 by Synopsys, Inc. All Rights Reserved.          0                                                                              2       1       1       1       8     HERTZ           v(0             v(vo            v(vs            i(vs            $&%#    ")

        with open(self.dir/'data_blocks_ac_9601.pickle', 'rb') as f:
            truth_blocks = pickle.load(f)
            self.assertEqual(data_blocks, truth_blocks)

    def test_parse_header(self):
        """
        the function that is being tested is dependant on parse_var_name and get_var_index
        :return:
        """
        header_str, _ = read_binary_signal_file(self.path)
        var_count, parsed_header = parse_header(header_str)
        self.assertEqual(parsed_header, ['HERTZ', 'v_0', 'v_vo', 'v_vs', 'i_vs'])
        self.assertEqual(5, var_count)

    def test_break_by_sweep(self):
        _, data_lst = read_binary_signal_file(self.path)
        data_lst = sum(data_lst, [])
        sweep_lst = break_by_sweep(data_lst, '9601')
        with open(self.dir/'sweep_lst_ac_9601.pickle', 'rb') as f:
            truth_blocks = pickle.load(f)
            self.assertTrue(sweep_lst == truth_blocks)

        self.assertTrue(len(sweep_lst) == 1)

    def test_general_make_dict(self):
        header_str, data_lst = read_binary_signal_file(self.path)
        sweep_lst = break_by_sweep(sum(data_lst, []), '9601')
        _, var_lst = parse_header(header_str)
        data_dict, _, _, _ = general_make_dict(var_lst, sweep_lst, header_str, False)  # the test file has no sweeps (break by sweep still has a purpose though
        with open(self.dir/'data_dict_ac_9601.pickle', 'rb') as f:
            truth_dict = pickle.load(f)
            self.assertEqual(data_dict, truth_dict)

    def test_write_to_dict(self):
        header_str, data_lst = read_binary_signal_file(self.path)
        data_dict, _, _, _ = write_to_dict(data_lst, header_str, 'tr')
        with open(self.dir/'data_dict_ac_9601.pickle', 'rb') as f:
            truth_dict = pickle.load(f)
            self.assertEqual(data_dict, truth_dict)

class TestDCSweepBin9601(ut.TestCase):
    """
    this tests the functions for getting to the dictionary structure for the 9601 format
    """
    def setUp(self) -> None:
        self.dir = Path(__file__).parent.resolve()
        self.path = self.dir/'test_9601.sw0'

    def test_is_binary(self):
        self.assertTrue(is_binary(self.path))

    def test_get_from_ext(self):
        self.assertEqual(get_from_ext(self.path), 'sw')

    def test_read_binary_signal_file(self):
        """
        the function that is being tested is dependant on read_data_block
        :return:
        """
        header_str, data_blocks = read_binary_signal_file(self.path)
        self.assertTrue(header_str == "00050000000000009601    * rccircuit.sp                                                  04/16/2021      00:57:08 Copyright (c) 1986 - 2021 by Synopsys, Inc. All Rights Reserved.          0                                                                              3       1       1       1       8     r1              v(0             v(vo            v(vs            i(vs            $&%#    ")

        with open(self.dir/'data_blocks_sw_9601.pickle', 'rb') as f:
            truth_blocks = pickle.load(f)
            self.assertTrue(data_blocks == truth_blocks)

    def test_parse_header(self):
        """
        the function that is being tested is dependant on parse_var_name and get_var_index
        :return:
        """
        header_str, _ = read_binary_signal_file(self.path)
        var_count, parsed_header = parse_header(header_str)
        self.assertEqual(parsed_header, ['r1', 'v_0', 'v_vo', 'v_vs', 'i_vs'])
        self.assertEqual(5, var_count)

    def test_break_by_sweep(self):
        _, data_lst = read_binary_signal_file(self.path)
        data_lst = sum(data_lst, [])
        sweep_lst = break_by_sweep(data_lst, '9601')
        with open(self.dir/'sweep_lst_sw_9601.pickle', 'rb') as f:
            truth_blocks = pickle.load(f)
            self.assertTrue(sweep_lst == truth_blocks)

        self.assertTrue(len(sweep_lst) == 1)

    def test_general_make_dict(self):
        header_str, data_lst = read_binary_signal_file(self.path)
        sweep_lst = break_by_sweep(sum(data_lst, []), '9601')
        _, var_lst = parse_header(header_str)
        data_dict, _, _, _ = general_make_dict(var_lst, sweep_lst, header_str, False)  # the test file has no sweeps (break by sweep still has a purpose though
        with open(self.dir/'data_dict_sw_9601.pickle', 'rb') as f:
            truth_dict = pickle.load(f)
            self.assertEqual(data_dict, truth_dict)

    def test_write_to_dict(self):
        header_str, data_lst = read_binary_signal_file(self.path)
        data_dict, _, _, _ = write_to_dict(data_lst, header_str, 'tr')
        with open(self.dir/'data_dict_sw_9601.pickle', 'rb') as f:
            truth_dict = pickle.load(f)
            self.assertEqual(data_dict, truth_dict)

class TestTranBin2001(ut.TestCase):
    """
    this tests the functions for getting to the dictionary structure for the 2001 format
    """
    def setUp(self) -> None:
        self.dir = Path(__file__).parent.resolve()
        self.path = self.dir/'test_2001.tr0'

    def test_is_binary(self):
        self.assertTrue(is_binary(self.path))

    def test_get_from_ext(self):
        self.assertEqual(get_from_ext(self.path), 'tr')

    def test_read_binary_signal_file(self):
        """
        the function that is being tested is dependant on read_data_block
        :return:
        """
        header_str, data_blocks = read_binary_signal_file(self.path)
        self.assertTrue(header_str == "000500000000000000002001* rccircuit.sp                                                  06/05/2020      15:22:51 Copyright (c) 1986 - 2020 by Synopsys, Inc. All Rights Reserved.          0                                                                              1       1       1       1       8     TIME            v(0             v(vo            v(vs            i(vs            $&%#    ")

        with open(self.dir/'data_blocks_tr_2001.pickle', 'rb') as f:
            truth_blocks = pickle.load(f)
            self.assertTrue(data_blocks == truth_blocks)

    def test_parse_header(self):
        """
        the function that is being tested is dependant on parse_var_name and get_var_index
        :return:
        """
        header_str, _ = read_binary_signal_file(self.path)
        var_count, parsed_header = parse_header(header_str)
        self.assertEqual(parsed_header, ['TIME', 'v_0', 'v_vo', 'v_vs', 'i_vs'])
        self.assertEqual(5, var_count)

    def test_break_by_sweep(self):
        _, data_lst = read_binary_signal_file(self.path)
        data_lst = sum(data_lst, [])
        sweep_lst = break_by_sweep(data_lst, '2001')
        with open(self.dir/'sweep_lst_tr_2001.pickle', 'rb') as f:
            truth_blocks = pickle.load(f)
            self.assertTrue(sweep_lst == truth_blocks)

        self.assertTrue(len(sweep_lst) == 1)

    def test_general_make_dict(self):
        header_str, data_lst = read_binary_signal_file(self.path)
        sweep_lst = break_by_sweep(sum(data_lst, []), '2001')
        _, var_lst = parse_header(header_str)
        data_dict, _, _, _ = general_make_dict(var_lst, sweep_lst, header_str, False)  # the test file has no sweeps (break by sweep still has a purpose though
        with open(self.dir/'data_dict_tr_2001.pickle', 'rb') as f:
            truth_dict = pickle.load(f)
            self.assertEqual(data_dict, truth_dict)

    def test_write_to_dict(self):
        header_str, data_lst = read_binary_signal_file(self.path)
        data_dict, _, _, _ = write_to_dict(data_lst, header_str, 'tr')
        with open(self.dir/'data_dict_tr_2001.pickle', 'rb') as f:
            truth_dict = pickle.load(f)
            self.assertEqual(data_dict, truth_dict)

if __name__ == '__main__':
    ut.main()